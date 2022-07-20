FROM python:3.10

WORKDIR /usr/app

COPY requirements.txt .

RUN pip install -r requirements.txt

# add entrypoint.sh
ADD ./entrypoint.sh /usr/app/entrypoint.sh

ENTRYPOINT ["sh", "./entrypoint.sh", "http://elasticsearch:9200"]
