import os
import sqlite3
import base64
import requests

# ❌ 하드코딩된 AWS Secret Key
AWS_SECRET_KEY = "AKIAZZZZZZZZZZZZZZZZ"

# ❌ SQL Injection
def authenticate(user, pwd):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user}' AND password = '{pwd}'"
    cursor.execute(query)
    return cursor.fetchone()

# ❌ 취약한 암호화 (Base64는 암호화 아님)
def encode(data):
    return base64.b64encode(data.encode()).decode()

# ❌ HTTPS 미사용
def send_data(data):
    requests.post("http://insecure-api.example.com", data={"payload": data})

user = input("Username: ")
pwd = input("Password: ")

authenticate(user, pwd)
print("Encoded password:", encode(pwd))
send_data(pwd)
