# syntax=docker/dockerfile:1
FROM python:3.10.6
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN pip --quiet install --upgrade pip
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
expose 8000
ENTRYPOINT ["./entrypoint.sh"]


