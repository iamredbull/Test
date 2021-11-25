FROM ubuntu
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone 
RUN apt-get update && apt-get install -y \
    build-essential \
    libtool \
    autotools-dev \
    automake \
    pkg-config \
    libssl-dev \
    libevent-dev \
    bsdmainutils \
    libboost-system-dev\
    libboost-filesystem-dev\
    libboost-chrono-dev\
    libboost-program-options-dev\
    libboost-test-dev\
    libboost-thread-dev\
    git 
RUN git clone https://github.com/dogecoin/dogecoin.git
RUN cd /dogecoin && ./autogen.sh && ./configure --disable-wallet && make && make install
RUN rm -r /dogecoin
CMD ["dogecoind","-printtoconsole", "-shrinkdebugfile"]
