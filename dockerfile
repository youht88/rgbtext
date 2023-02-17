FROM python:3.8-slim-buster

ENV LANG en_US.UTF-8 LC_ALL=en_US.UTF-8
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /opt
RUN apt update \
    && apt install libgl1-mesa-glx libglib2.0-0 -y \
    && apt install gcc -y

COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple/\
    && pip3 install --no-cache-dir -r requirements.txt --default-timeout=100 --extra-index-url https://pypi.tuna.tsinghua.edu.cn/simple/ \
    && rm -rf /tmp/* && rm -rf /root/.cache/* \
    && sed -i 's#http://deb.debian.org#http://mirrors.aliyun.com/#g' /etc/apt/sources.list\
    && apt-get --allow-releaseinfo-change update

COPY ./* ./
RUN echo "python3 ./app.py > /opt/`date +"%y-%m-%d_%H:%M"`.out " >> /opt/start.sh && \
    chmod 755 /opt/start.sh
CMD /opt/start.sh

