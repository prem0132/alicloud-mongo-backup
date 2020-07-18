FROM python:buster
WORKDIR /app
ADD requirements.txt ./requirements.txt
RUN pip install -r requirements.txt
ADD . .
ENTRYPOINT ["python", "main.py"]