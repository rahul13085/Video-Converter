FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN curl -L https://johnvansickle.com/ffmpeg/builds/ffmpeg-release-amd64-static.tar.xz | tar -xJf - && mv ffmpeg-release-amd64-static/ffmpeg /usr/local/bin/

ENTRYPOINT ["python", "main.py"]