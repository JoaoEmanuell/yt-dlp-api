FROM python:3.11-alpine

RUN pip --no-cache-dir install --upgrade pip

# Create no root user

RUN apk add --no-cache bash && apk add --no-cache shadow && apk add --no-cache p7zip

ENV NO_ROOT_USER=python
ENV NO_ROOT_USER_PASSWORD=python

RUN useradd -m $NO_ROOT_USER

RUN echo "$NO_ROOT_USER:$NO_ROOT_USER_PASSWORD" | chpasswd

# Add permissions to install packges

RUN chmod -R a+rw /home/python

# Set workdir

WORKDIR /usr/src/app

RUN chmod -R a+rw /usr/src/app

RUN apk del shadow

RUN chown -R $NO_ROOT_USER /usr/src/app 

# Config no root env

ENV HOME="/home/python"

ENV PATH="$PATH:$HOME/.local/bin"

# Ports and run

EXPOSE 8080

COPY . /usr/src/app

RUN pip --no-cache-dir install -r requirements.txt

RUN python setup_initial.py

USER $NO_ROOT_USER

ENTRYPOINT [ "flask" ]

CMD [ "run", "--host", "0.0.0.0", "--port", "8080"]