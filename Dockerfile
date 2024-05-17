FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN curl -L https://ffmpeg.org/releases/ffmpeg-7.0.tar.xz | tar -xJf - && mv ffmpeg-release-amd64-static/ffmpeg /usr/local/bin/

ENTRYPOINT ["python", "main.py"]
