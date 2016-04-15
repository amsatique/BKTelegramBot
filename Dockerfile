FROM ubuntu
MAINTAINER KivinKvn
RUN apt-get update
RUN apt-get -y install python3 git wget
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py

COPY BK /BK
WORKDIR /BK
RUN pip install -r requirements.txt
CMD ["python3", "bot.py"]