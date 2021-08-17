FROM ubuntu:20.04
ENV LC_CTYPE C.UTF-8
ARG DEBIAN_FRONTEND=noninteractive
# Updating and installing git, gdb, python3 vim and useful tools that we'll need

RUN apt-get update && apt-get install -yq gcc make wget curl git vim gdb python3 python3-pip bsdmainutils

# Downloading and compiling old sudo version

RUN cd /root/ && wget https://www.sudo.ws/dist/sudo-1.8.31p2.tar.gz && tar -xvf sudo-1.8.31p2.tar.gz && cd sudo-1.8.31p2 && export CFLAGS="-ggdb" && ./configure && make && make install

# Adding the user account

RUN useradd -ms /bin/bash user
RUN echo 'export PS1="\[\e]0;\u@\h: \w\a\]\[\033[01;31m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]# "' >> /root/.bashrc
RUN echo 'export PS1="\[\e]0;\u@\h: \w\a\]\[\033[01;32m\]\u\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]$ "' >> /home/user/.bashrc
USER user

# Setting the working directory

WORKDIR /home/user
