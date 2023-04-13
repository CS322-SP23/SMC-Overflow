FROM ubuntu:20.04
RUN apt -y update && apt -y upgrade
RUN apt -y install sudo
RUN sudo apt -y install git
##RUN git config --global user.email "your email"
##RUN git config --global user.name "your username"
# RUN yes| unminimize
ARG DEBIAN_FRONTEND=noninteractive

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


RUN pip install flask
RUN pip install psycopg2-binary


RUN apt -y install  postgresql postgresql-contrib
RUN service postgresql start


# ENV POSTGRES_USER=myuser
# ENV POSTGRES_PASSWORD=mypassword
# ENV POSTGRES_DB=mydatabase

WORKDIR /workspaces/SMC-Overflow/ 
# ENTRYPOINT ["sh", "setup"]

# create user which will execute server, username smc, 
# server should not have sudoer priviledges if at all possible
# will fully configure when nearing end
# RUN mkdir workspaces
# RUN adduser --disabled-password -- '' smc
# RUN chown -R smc:smc /workspaces

# RUN pg_createcluster -u smc 


#once the user is changes as no more install scripts should be ran
#only scripts which relate to the running of the server
# USER smc


# RUN flask run
