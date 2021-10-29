FROM python:3.8

COPY entrypoint.sh /entrypoint.sh
COPY validate.py /validate.py
COPY requirements.txt /requirements.txt

RUN ["chmod", "+x" ,"/entrypoint.sh"]
RUN ["pip", "install", "--upgrade", "pip"]
RUN ["pip", "install", "-r", "/requirements.txt"]

ENTRYPOINT ["/entrypoint.sh"]
