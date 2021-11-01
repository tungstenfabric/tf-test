FROM centos:7.4.1708

ARG SITE_MIRROR

# back up mirrors before overwriting
RUN cp -r /etc/yum.repos.d /etc/yum.repos.d.orig

# prepare custom mirrors
COPY *.repo Dockerfile /etc/yum.repos.d/

# pip install python packages
COPY *requirements*.txt entrypoint.sh /
COPY pip.conf /etc/

# 1. install most packages from pypi and only then python-Fabric
RUN \
    yum install -y unzip vim tcpdump ant git ipmitool gcc python-devel \
      patch sshpass bzip2 wget sudo pexpect ant-junit libXpm libXrender \
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
