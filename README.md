# Container installer

This program will simply build and dploy Docker container from Dockerfile

## For running of that program which will deploy your container on local machine you will need:

1) Preinstalled Docker.io

For Ubuntu

```bash
sudo apt get docker.io
```
For CentOS
```bash
sudo yum install docker.io
```
2) Preinstalled and configured Git. Git should be in your PATH. SSH key's should works. Your name and e-mail should be configured

For Ubuntu
```bash
sudo apt install git
```
For CentOS
```bash
sudo yum install git
```

3) Python 3.8 or higher. I have test it on python3.8. 

For Ubuntu
```bash
sudo apt install python3.8
```
For CentOS
```bash
sudo yum install python3.8
```

4) List of python modules from requirments file (easiest way to get them -- "")
```pip
pip install -r requirements.txt
```

## Run programm with python

You can check result on port which you have mention in your app. In this case it is 8080.

```bash
sudo python3.8 candidate.py
```
