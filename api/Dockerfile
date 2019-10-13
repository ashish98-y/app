FROM python:3.4-alpine
COPY app.py ./app/app.py
WORKDIR /app
RUN pip install flask
ENTRYPOINT python app.py
