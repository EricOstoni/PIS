
FROM python:3.8-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5001

ENV FLASK_ENV=production

CMD ["flask", "run", "--host=0.0.0.0"]
