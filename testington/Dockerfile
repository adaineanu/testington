FROM python:3.6-slim

WORKDIR /

ADD /src /app

ADD entrypoint.sh /

ADD /migration /migration

ADD requirements.txt /

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

ENV NAME World

ENTRYPOINT ["sh", "entrypoint.sh"]
