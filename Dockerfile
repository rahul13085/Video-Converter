FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY . .

RUN mkdir -p /usr/local/bin
RUN grep -i 'error\|warning' download_extraction.log && exit 1
RUN curl -L https://ffmpeg.org/releases/ffmpeg-7.0.tar.xz | tar -xJf - 2>&1 | tee download_extraction.log

RUN grep -i error download_extraction.log && exit 1

RUN curl -L https://ffmpeg.org/releases/ffmpeg-7.0.tar.xz | tar -xJf - && \
    cd ffmpeg && \
    ./configure --enable-libass --enable-gpl --enable-libvorbis --enable-libx264 --enable-libx265 && \
    make -j $(nproc) && \
    make install && \
    cp ffmpeg /usr/local/bin/

ENTRYPOINT ["python", "main.py"]
