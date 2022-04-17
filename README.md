Battleship

This is the django project for battleship game


Run this commands to create virtualenv: python3 -m venv venv . venv/bin/activate pip install -r requirements.txt

Run this command to create .env: touch .env

Write your credentials in .env 

Open postgresql: psql 

Create database, which you wrote in .env DB_NAME

Start Redis server

Run this commands to update your database: python3 manage.py migrate

Run this command to start server: python3 manage.py runserver

It can be accessed in http://localhost:8000/

