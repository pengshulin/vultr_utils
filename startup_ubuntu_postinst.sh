#!/bin/sh
# post install script for vultr instance
# Peng Shulin <trees_peng@163.com> 2018

cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
apt-get update
apt-get -y upgrade

echo -e "\nexport LC_ALL=C\n" >> /root/.bashrc
export LC_ALL=C

apt-get install -y tmux vim git htop traceroute nmap
apt-get install -y python 
apt-get install -y python-setuptools
apt-get install -y python-pip
pip install --upgrade pip
pip install lxml beautifulsoup4 shadowsocks pysocks netifaces
pip install --upgrade requests

apt-get install -y mosquitto
