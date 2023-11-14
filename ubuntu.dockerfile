FROM ubuntu:jammy

RUN apt update

RUN apt install nano

RUN apt install curl -y

RUN apt install systemctl -y

RUN apt install git -y

WORKDIR /var/www/html

ENTRYPOINT ["tail", "-f", "/dev/null"]