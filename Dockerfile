FROM python:3            
ENV PYTHONUNBUFFERED 1           
WORKDIR /code           
COPY requirements.txt /code/
RUN apt-get update -y  && apt-get upgrade -y && apt-get install curl
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/            
EXPOSE 8000