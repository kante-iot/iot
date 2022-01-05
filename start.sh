#!/bin/sh
# 기본 라이브러리 업데이트
sudo apt-get update
sudo apt-get upgrade
# 파이썬 설치
sudo apt-get install python3-dev python3-pip -y
# pip 온습도계 관련 라이브러리 설치
sudo python3 -m pip install --upgrade pip setuptools wheel -y

# 온습도계 라이브러리 git clone
git clone https://github.com/kante-iot/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT/

# 온습도계 라이브러리 설치
sudo python3 setup.py install
