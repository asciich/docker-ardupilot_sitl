FROM ubuntu:16.04

MAINTAINER Reto Hasler <reto.hasler@asciich.ch>

RUN apt-get update && \
    apt-get install -y \
        git \
        python-matplotlib \
        python-serial \
        python-matplotlib \
        python-serial \
        python-wxgtk3.0 \
        python-wxtools \
        python-lxml \
        python-scipy \
        python-opencv \
        ccache \
        gawk \
        git \
        python-pip \
        python-pexpect \
        x11-apps \
        expect \
        vim \
    && \
    pip install --upgrade pip
RUN pip install --upgrade setuptools && \
    pip install --upgrade \
        future \
    && \
    pip install \
        pymavlink \
        MAVProxy \
    && \
    cd / && \
    git clone git://github.com/ArduPilot/ardupilot.git && \
    cd ardupilot && \
    git checkout Copter-3.5.5 && \
    git submodule update --init --recursive && \
    cd / \
    && \
    echo "export PATH=\$PATH:/ardupilot/Tools/autotest" >> /root/.bashrc && \
    echo "export PATH=/usr/lib/ccache:\$PATH" >> /root/.bashrc

ENV PATH=$PATH:/ardupilot/Tools/autotest
ENV PATH=/usr/lib/ccache:$PATH

COPY ./files/wipe_scripts/* /
COPY ./files/* /

RUN apt-get install -y \
        libtool \
        libtool-bin \
        automake \
        autoconf \
        libexpat1-dev

RUN git clone git://github.com/tridge/jsbsim.git

RUN cd jsbsim && \
    ./autogen.sh --enable-libraries && \
    make

ENV PATH=$PATH:/jsbsim/src


RUN for SCRIPT in $(ls /*.sh) ; do \
        chmod +x ${SCRIPT} && \
        DEST=$(echo $SCRIPT | sed 's#.sh##g') && \
        mv -v ${SCRIPT} /usr/bin/${DEST} \
    ; done && \
    \
    for SCRIPT in $(ls /*.expect) ; do \
        chmod +x ${SCRIPT} && \
        mv -v ${SCRIPT} /usr/bin/. \
    ; done

RUN wipe_sitl_arducopter && \
    wipe_sitl_arduplane && \
    mkdir -p /var/log/mavproxy/
