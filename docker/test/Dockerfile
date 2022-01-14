ARG REGISTRY_SERVER=localhost:5000
ARG BASE_TAG=latest
FROM $REGISTRY_SERVER/contrail-test-base:$BASE_TAG
ARG SKU=ocata
ARG OPENSTACK_REPO
ARG CONTRAIL_REPO
ARG DOCKERFILE_DIR

COPY $DOCKERFILE_DIR/*requirements*.txt $DOCKERFILE_DIR/*.rpm /

RUN cp -r /etc/yum.repos.d /etc/yum.repos.d.orig && \
    mkdir -p /contrail-test
COPY $DOCKERFILE_DIR/*.repo $DOCKERFILE_DIR/prepare_repos.sh /etc/yum.repos.d/
COPY ./ /contrail-test/

# install bash curl and other rpm for upgrade to versions without vulnerabilities
RUN /etc/yum.repos.d/prepare_repos.sh && \
    yum install -y bash curl expat gobject-introspection libxml2 procps-ng yum-utils && \
    yum install -y python-contrail python3-contrail && \
    yum clean all -y && rm -rf /var/cache/yum && \
    if [[ "$ID" == 'centos' ]] ; then \
      python2 -m pip install -r /indirect_requirements_centos.txt ; \
    fi && \
    python2 -m pip install  -r /indirect_requirements.txt -r /requirements.txt && \
    python3 -m pip install -r /indirect_requirements3.txt -r /requirements.txt -r /requirements3.txt && \
    rm -rf /etc/yum.repos.d && \
    mv /etc/yum.repos.d.orig /etc/yum.repos.d && \
    mkdir -p /contrail-test/images

ENTRYPOINT ["/entrypoint.sh"]

LABEL net.juniper.contrail=test
LABEL net.juniper.node=test
