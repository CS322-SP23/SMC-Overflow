FROM ubuntu/postgres:14-22.04_edge
RUN apt update && apt upgrade
RUN apt install sudo
RUN sudo apt install git
##RUN git config --global user.email "your email"
##RUN git config --global user.name "your username"
RUN sudo apt install python3
RUN sudo apt install python3-pip
RUN apt-get install libpq-dev
RUN pip install -r requirements.txt
