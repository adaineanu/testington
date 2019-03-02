FROM postgres

RUN apt-get update

RUN apt-get install -y python3-pip

WORKDIR /

ADD /src /app

ADD entrypoint.sh /

ADD /migration /migration

ADD requirements.txt /

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 8080

ENV NAME World

ENTRYPOINT ["sh", "entrypoint.sh"]
