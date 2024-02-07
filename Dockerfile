FROM node:20 AS frontend
WORKDIR /opt/frontend
COPY frontend/package.json .
RUN npm install
COPY frontend/ .
RUN npm run build

FROM python:3.11-bookworm
WORKDIR /opt/server
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .
COPY --from=frontend /opt/frontend/build/ ./static
ENTRYPOINT gunicorn server:app --bind=0.0.0.0:8080 --log-level debug
