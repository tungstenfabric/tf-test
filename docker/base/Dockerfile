ARG LINUX_DISTR=centos
ARG LINUX_DISTR_VER=7.4.1708
FROM $LINUX_DISTR:$LINUX_DISTR_VER

ARG SITE_MIRROR
ARG YUM_ENABLE_REPOS=""

# back up mirrors before overwriting
RUN cp -r /etc/yum.repos.d /etc/yum.repos.d.orig

# prepare custom mirrors
COPY *.repo Dockerfile /etc/yum.repos.d/

# pip install python packages
COPY *requirements*.txt entrypoint.sh /
COPY pip.conf /etc/

# 1. install most packages from pypi and only then python-Fabric
RUN \
    source /etc/os-release && \
    if [[ "$ID" == 'rhel' && "$VERSION_ID" == '8.4' ]] ; then \
      YUM_ENABLE_REPOS=$(echo $YUM_ENABLE_REPOS | tr -d '"') && \
      if [[ -n "$YUM_ENABLE_REPOS" ]] ; then \
          echo "INFO: contrail-test-base: enable repos $YUM_ENABLE_REPOS" && \
          if ! type -p yum-config-manager ; then \
              yum install -y yum-utils ; \
          fi && \
          yum-config-manager --enable $YUM_ENABLE_REPOS && \
          yum clean metadata ; \
      fi && \
      yum module enable -y javapackages-tools ; \
    fi && \
    yum install -y unzip vim tcpdump ant git ipmitool gcc python2-devel \
      patch sshpass bzip2 wget sudo ant-junit libXpm libXrender \
      gtk2 nss GConf2 openssl && \
    wget -nv -c --tries=3 -O /tmp/get-pip.py ${SITE_MIRROR:-"https://bootstrap.pypa.io"}/pip/2.7/get-pip.py && \
    python2 /tmp/get-pip.py 'pip==20.1' && \
    yum install -y python3 python3-devel && \
    python2 -m pip install -r /indirect_requirements.txt -r /requirements.txt && \
    python3 -m pip install -r /indirect_requirements3.txt -r /requirements3.txt && \
    yum clean all -y && \
    rm -rf /var/cache/yum && \
    rm -rf /etc/yum.repos.d && \
    mv /etc/yum.repos.d.orig /etc/yum.repos.d
