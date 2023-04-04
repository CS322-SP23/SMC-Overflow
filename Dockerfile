FROM ubuntu/postgres:14-22.04_edge
RUN apt update && apt upgrade
RUN apt install sudo
RUN sudo apt -y install git
##RUN git config --global user.email "your email"
##RUN git config --global user.name "your username"
RUN sudo apt -y install python3
RUN sudo apt -y install python3-pip
RUN apt-get -y install libpq-dev
RUN nvm install node
