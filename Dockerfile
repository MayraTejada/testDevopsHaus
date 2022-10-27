FROM python:buster

WORKDIR /usr/src/app
COPY . .
CMD ["sudo", "apt-get", "install", "libmysqlclient-dev"]
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "application.py" ]