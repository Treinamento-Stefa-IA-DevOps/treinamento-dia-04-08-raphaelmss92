# FROM python:3.8-slim
FROM centos/python-36-centos7

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "80", "--reload"]