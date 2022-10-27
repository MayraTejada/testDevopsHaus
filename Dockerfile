FROM python:buster


COPY . .

RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "application.py" ]