#!/bin/bash

# TODO: move CONTRAIL_REPO from test-test to test-base to decrease time build

REGISTRY_SERVER="opencontrail"
SKU=""
CONTRAIL_REPO=""
OPENSTACK_REPO=""
TAG=""

LINUX_ID=$(awk -F"=" '/^ID=/{print $2}' /etc/os-release | tr -d '"')
LINUX_VER_ID=$(awk -F"=" '/^VERSION_ID=/{print $2}' /etc/os-release | tr -d '"')

#SITE_MIRROR is an URL to the root of cache. This code will look for the files inside predefined folder
[ -z "${SITE_MIRROR}" ] || SITE_MIRROR="${SITE_MIRROR}/external-web-cache"

download_pkg () {
    local pkg=$1
    local dir=$2
    if [[ $pkg =~ ^http[s]*:// ]]; then
        wget --spider $pkg
        filename="${pkg##*/}"
        wget $pkg -O $dir/$filename
    elif [[ $pkg =~ ^ssh[s]*:// ]]; then
        server=$(echo $pkg | sed 's=scp://==;s|\/.*||')
        path=$(echo $pkg |sed -r 's#scp://[a-zA-Z0-9_\.\-]+##')
        yum install -y sshpass
        sshpass -e scp -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null ${sshuser_sub}${server}:${path} $dir
    else
        echo "ERROR, Unknown url format, only http[s], ssh supported" >&2
        exit 1
    fi
}

docker_build_test_sku () {
    local dir=${1%/}
    local name=$2
    local tag=$3
    local build_arg_opts='--network host'
    local dockerfile=${dir}'/Dockerfile'
    docker_ver=$(sudo docker -v | awk -F' ' '{print $3}' | sed 's/,//g')
    if [[ "$docker_ver" < '17.06' ]] ; then
        cat $dockerfile | sed \
        -e 's/\(^ARG REGISTRY_SERVER=.*\)/#\1/' \
        -e "s|\$REGISTRY_SERVER|${REGISTRY_SERVER}|g" \
        -e 's/\(^ARG BASE_TAG=.*\)/#\1/' \
        -e "s/\$BASE_TAG/$BASE_TAG/g" \
        > ${dockerfile}.nofromargs
        dockerfile="${dockerfile}.nofromargs"
    else
        build_arg_opts+=" --build-arg REGISTRY_SERVER=${REGISTRY_SERVER}"
        build_arg_opts+=" --build-arg BASE_TAG=${BASE_TAG}"
    fi
    build_arg_opts+=" --build-arg SKU=${SKU}"
    build_arg_opts+=" --build-arg CONTRAIL_REPO=${CONTRAIL_REPO}"
    build_arg_opts+=" --build-arg OPENSTACK_REPO=${OPENSTACK_REPO}"
    build_arg_opts+=" --build-arg DOCKERFILE_DIR=${dir}"
    [ -z "$SITE_MIRROR" ] || build_arg_opts+=" --build-arg SITE_MIRROR=${SITE_MIRROR}"
    if [[ "$LINUX_ID" == 'rhel' && "${LINUX_VER_ID//.[0-9]*/}" == '8' ]] ; then
        # podman case
        build_arg_opts+=' -v /etc/resolv.conf:/etc/resolv.conf:ro'
    fi
    echo "Building test container ${name}:${tag} with opts ${build_arg_opts}"
    sudo docker build ${build_arg_opts} -t ${name}:${tag} -f $dockerfile . || exit 1
    echo "Built test container ${name}:${tag}"
}

docker_build_test () {
    usage () {
    cat <<EOF
Build test container

Usage: $0 test [OPTIONS]

  -h|--help                     Print help message
  --tag           TAG           Docker container tag, default to sku
  --base-tag      BASE_TAG      Specify contrail-base-test container tag to use. Defaults to 'latest'.
  --sku           SKU           Openstack version. Defaults to ocata
  --contrail-repo CONTRAIL_REPO Contrail Repository, mandatory
  --openstack-repo OPENSTACK_REPO Openstack Repository, mandatory
  --registry-server REGISTRY_SERVER Docker registry hosting the base test container, Defaults to docker.io/opencontrail
  --post          POST          Upload the test container to the registy-server, if specified
EOF
    }
    if ! options=$(getopt -o h -l help,base-tag:,tag:,sku:,contrail-repo:,openstack-repo:,package-url:,registry-server:,post -- "$@"); then
        usage
        exit 1
    fi
    eval set -- "$options"

    while [ $# -gt 0 ]; do
        case "$1" in
            -h|--help) usage; exit;;
            --base-tag) BASE_TAG=$2; shift;;
            --tag) TAG=$2; shift;;
            --sku) SKU=$2; shift;;
            --contrail-repo) CONTRAIL_REPO=$2; shift;;
            --openstack-repo) OPENSTACK_REPO=$2; shift;;
            --registry-server) REGISTRY_SERVER=$2; shift;;
            --post) POST=1; shift;;
        esac
        shift
    done

    if [[ -z $CONTRAIL_REPO ]]; then
        echo "Need to specify either --contrail-repo"; echo
        usage
        exit 1
    fi
    if [[ -z $REGISTRY_SERVER ]]; then
        echo "--registry-server is unspecified, using docker.io/opencontrail"; echo
    fi
    if [[ -z $SKU ]]; then
        echo "SKU(--sku) is unspecified. Assuming ocata"; echo
        SKU=ocata
    fi
    if [[ -z $TAG ]]; then
        echo "TAG(--tag) is unspecified. using $SKU"; echo
        TAG=$SKU
    fi
    if [[ -z $BASE_TAG ]]; then
        echo "BASE_TAG(--base-tag) is unspecified, using 'latest'."; echo
        BASE_TAG='latest'
    fi
    if [[ -z $OPENSTACK_REPO ]]; then
        OPENSTACK_REPO="http://mirror.centos.org/centos/7/cloud/x86_64/openstack-${SKU}"
    fi

    docker_build_test_sku "docker/test" "contrail-test-test" "$TAG"
    sudo docker tag contrail-test-test:$TAG $REGISTRY_SERVER/contrail-test-test:$TAG
    if [[ -n $POST ]]; then
        sudo docker push $REGISTRY_SERVER/contrail-test-test:$TAG
    fi
}

docker_build_base () {
    REGISTRY_SERVER=""
    usage () {
    cat <<EOF
Build base container

Usage: $0 base
  -h|--help                     Print help message
  --registry-server REGISTRY_SERVER Docker registry hosting the base test container, specify if the image needs to be pushed
  --tag             TAG           Docker container tag, default to sku
  --post            POST          Upload the test container to the registy-server, if specified
EOF
    }
    if ! options=$(getopt -o h -l help,post,registry-server:,tag: -- "$@"); then
        usage
        exit 1
    fi
    eval set -- "$options"
    while [ $# -gt 0 ]; do
        case "$1" in
            -h|--help) usage; exit;;
            --tag) TAG=$2; shift;;
            --registry-server) REGISTRY_SERVER=$2; shift;;
            --post) POST=1; shift;;
        esac
        shift
    done
    if [[ -z $TAG ]]; then
        echo "TAG(--tag) is unspecified. using latest"; echo
        TAG=latest
    fi
    local build_arg_opts="--network host"
    [ -z "$SITE_MIRROR" ] || build_arg_opts+=" --build-arg SITE_MIRROR=${SITE_MIRROR}"
    if [[ "$LINUX_ID" == 'rhel' && "${LINUX_VER_ID//.[0-9]*/}" == '8' ]] ; then
        # podman case
        build_arg_opts+=' -v /etc/resolv.conf:/etc/resolv.conf:ro'
    fi
    echo "Building base container (build_arg_opts=$build_arg_opts)"
    sudo docker build $build_arg_opts -t contrail-test-base:$TAG docker/base || exit 1
    if [[ -n $REGISTRY_SERVER ]]; then
        sudo docker tag contrail-test-base:$TAG $REGISTRY_SERVER/contrail-test-base:$TAG
    fi
    if [[ -n $POST ]]; then
        sudo docker push $REGISTRY_SERVER/contrail-test-base:$TAG
    fi
    echo "Built base container contrail-test-base:$TAG"
}

usage () {
    cat <<EOF
Build of contrail test container

Usage: $0 (base|test) [OPTIONS]

Subcommands:

base   Build base test container which is openstack/contrail version agnostic
test   Build contrail test container openstack/contrail version specific

Run $0 <Subcommand> -h|--help to get subcommand specific help

EOF
}

if [[ -n $SSHUSER ]]; then
   sshuser_sub="${SSHUSER}@"
fi
subcommand=$1; shift;
if [[ $subcommand == '-h' || $subcommand == '' || $subcommand == '--help' ]]; then
    usage
    exit
elif [[ $subcommand == 'test' ]]; then
    docker_build_test $@
elif [[ $subcommand == 'base' ]]; then
    docker_build_base $@
else
    echo "Error: '$subcommand' is not a known subcommand." >&2
    echo "       Run '$0 --help' for a list of known subcommands." >&2
    exit 1
fi
