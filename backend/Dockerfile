FROM python:3.11-bookworm
WORKDIR /opt/api
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT gunicorn api:app --bind=0.0.0.0:8080
