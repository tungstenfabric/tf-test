FROM centos:7.9.2009

ARG SITE_MIRROR

# back up mirrors before overwriting
RUN cp -r /etc/yum.repos.d /etc/yum.repos.d.orig

# prepare custom mirrors
COPY *.repo Dockerfile /etc/yum.repos.d/

# pip install python packages
COPY *requirements*.txt entrypoint.sh /
COPY pip.conf /etc/

# install most packages from pypi and only then python-Fabric
RUN \
    curl --retry 3 --retry-delay 10 ${SITE_MIRROR:-"https://bootstrap.pypa.io"}/pip/2.7/get-pip.py | python2 - 'pip==20.1' && \
    yum install -y unzip vim tcpdump ant git ipmitool gcc python-devel \
      patch sshpass bzip2 wget sudo pexpect ant-junit libXpm libXrender \
      gtk2 nss GConf2 openssl python3 python3-devel && \
    yum update -y -x "centos-release*" -x "coreutils*" -x "net-snmp-libs" && \
    yum -y update-minimal --security --sec-severity=Important --sec-severity=Critical && \
    pip install -r /indirect_requirements.txt -r /requirements.txt && \
    pip3 install -r /indirect_requirements3.txt -r /requirements3.txt && \
    yum clean all -y && \
    rm -rf /var/cache/yum && \
    rm -rf /etc/yum.repos.d && \
    mv /etc/yum.repos.d.orig /etc/yum.repos.d
