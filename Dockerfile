FROM python:3.6-alpine

# 将当前目录复制到容器的 code 目录
WORKDIR /code
ADD . /code/

RUN apk update && apk add \
        libuuid \
        pcre \
        mailcap \
        gcc \
        libc-dev \
        linux-headers \
        pcre-dev \
    && pip install pip -U \
    && pip install -r requirements.txt \
    && apk del \
        gcc \
        libc-dev \
        linux-headers \
    && rm -rf /tmp/*

##
EXPOSE 8000

RUN python3 manage.py makemigrations  && python3 manage.py migrate

CMD [ "uwsgi", "--ini", "uwsgi.ini"]
#CMD [ "python", "manage.py", "runserver","0.0.0.0:8000" ]
