# Flask Blog 
It's my personal blog code  
Here soon <- will be link to my website

# Installation 
There are two ways to install this project \
1.Use docker-compose
In project directory 
```python
python3 generate_config.py
```
If you wanna run Flask server in debug mode change 
variable env to production in .env file 
```docker
docker-compose build
docker-compose up -d
```
Server should be running in 127.0.0.1:5000

2.Use python 
```python
python3 -m venv venv 
pip3 install -r requirements.txt
python3 generate_config.py
export FLASK_APP=app.py
python3 -m flask run
```
If you wanna run Flask server in debug mode change 
variable env to production in .env file  \
Change MONGO_URI to your mongoDB server adress

# Contribution 
Fell free to add pull requests

# contact
Create a issue or write to me nero2310.kontakt@protonmail.com