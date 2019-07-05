FROM python:2.7

RUN apt-get update && apt-get install -y mysql-client

RUN mkdir /etl-export
COPY * /etl-export

WORKDIR /etl-export
RUN ./setup.sh

CMD ./export.sh
