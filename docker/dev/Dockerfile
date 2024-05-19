FROM python:3.11-alpine

RUN pip install --upgrade pip

# Create no root user

RUN apk add --no-cache bash && apk add --no-cache shadow && apk add --no-cache p7zip

ENV NO_ROOT_USER=python
ENV NO_ROOT_USER_PASSWORD=python

RUN useradd -m $NO_ROOT_USER

RUN echo "$NO_ROOT_USER:$NO_ROOT_USER_PASSWORD" | chpasswd

# Add permissions to install packges

RUN chmod -R a+rw /home/python

# Set user and workdir

USER $NO_ROOT_USER

WORKDIR /usr/src/app

# Config no root env

ENV HOME="/home/python"

ENV PATH="$PATH:$HOME/.local/bin"

# Ports and run

EXPOSE 8080

CMD tail -f /dev/null