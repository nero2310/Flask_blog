FROM python:3.8

WORKDIR /usr/src/web_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3","app.py"]

