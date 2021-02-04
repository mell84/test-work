FROM ubuntu:latest
MAINTAINER Aleksey Melnikov 
RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev build-essential libpq-dev
COPY . /app
COPY requirements.txt /app 
WORKDIR /app
RUN pip3 install -r /app/requirements.txt
ENTRYPOINT ["python3"]
CMD ["make_database.py"]
