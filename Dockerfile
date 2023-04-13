FROM ubuntu:20.04

RUN apt -y update && apt -y upgrade
RUN apt install sudo
RUN sudo apt -y install git


RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone

ARG DEBIAN_FRONTEND=noninteractive

#RUN git config --global user.email "your email"
#RUN git config --global user.name "your username"
RUN sudo apt -y install python3
RUN sudo apt -y install python3-pip
RUN apt-get -y install libpq-dev
RUN sudo apt -y install nodejs
#RUN sudo apt -y install npm
RUN pip install flask
RUN pip install psycopg2-binary





RUN sudo apt -y install python3
RUN sudo apt -y install python3-pip

# RUN apt-get install -y software-properties-common
# RUN add-apt-repository universe
# RUN apt-get update

RUN apt-get -y install libpq-dev
RUN apt-get -y install curl
RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
RUN apt -y install acl
RUN export NVM_DIR="$HOME/.nvm" && \
    [ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh" && \
    [ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion" && \
    nvm install node


RUN apt -y install  postgresql postgresql-contrib
WORKDIR /workspaces/SMC-Overflow/ 

