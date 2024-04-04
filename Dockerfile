FROM node:20 AS frontend
WORKDIR /opt/frontend
COPY frontend/package.json .
RUN npm install
COPY frontend/ .
RUN npm run build

FROM python:3.11-bookworm
WORKDIR /app
COPY backend/requirements.txt .
RUN pip install -r requirements.txt
COPY backend/ .
# There's gotta bea better way to do this
COPY --from=frontend /opt/frontend/build/200.html .
COPY --from=frontend /opt/frontend/build/favicon.png .
COPY --from=frontend /opt/frontend/build/static ./static

ENTRYPOINT gunicorn server:app --bind=0.0.0.0:8080 --workers=5
