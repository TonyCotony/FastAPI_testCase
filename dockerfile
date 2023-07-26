FROM python:3.9

WORKDIR .
COPY requirements.txt
#WORKDIR /media/docker_images/web
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python3 create_tables.py