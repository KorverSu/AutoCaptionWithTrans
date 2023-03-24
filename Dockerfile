FROM ubuntu
WORKDIR /app

RUN mkdir font templates mp4 result srt_file
COPY app.py caption.py video.py ./
COPY font ./font
COPY templates ./templates

RUN apt update
RUN apt install -y python3
RUN apt update
RUN apt install -y python3-pip

RUN pip3 install --no-cache-dir googletrans==4.0.0rc1 moviepy==1.0.3 Pillow==9.4.0 Flask==2.2.3 -U openai-whisper

RUN apt update
RUN apt install -y ffmpeg
RUN pip3 install setuptools-rust
RUN apt update
RUN apt install -y rustc
EXPOSE 5000
CMD python3 app.py