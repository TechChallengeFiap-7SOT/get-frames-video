FROM python:3.12.9-alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apk add  --no-cache ffmpeg

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "mainQueue.py"]