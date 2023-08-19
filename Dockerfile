FROM python:3.8-slim-buster

#https://grigorkh.medium.com/fix-tzdata-hangs-docker-image-build-cdb52cc3360d
#ENV TZ=Asia/Kolkata
#RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /Video-Summarisation-Project

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

#RUN apt update -y && apt install ffmpeg libsm6 libxext6  -y

#Gmail APIs
#RUN pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

COPY . .

CMD [ "python3", "-m" , "flask", "--app", "VideoSummarisation", "run", "--host=0.0.0.0"]
