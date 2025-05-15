import sqlite3
import base64
import os
import requests

# 🔐 하드코딩된 비밀 키 (Secrets 탐지)
API_KEY = "sk_test_51Hx3nLZ0SecretKeyForTesting123"

# 🔓 환경변수 노출 테스트
DB_PASSWORD = os.getenv("DB_PASSWORD", "default_db_password")

def login(username, password):
    # ❌ SQL Injection 취약점
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()
    return result

def get_data():
    # ❌ HTTPS 미사용 API 호출
    response = requests.get("http://insecure-api.example.com/data")
    return response.text

def encode_password(password):
    # ❌ 암호화 아님: base64는 encoding
    return base64.b64encode(password.encode('utf-8')).decode('utf-8')

if __name__ == "__main__":
    username = input("Username: ")
    password = input("Password: ")
    result = login(username, password)
    if result:
        print("Login successful")
    else:
        print("Login failed")

    encoded = encode_password(password)
    print(f"Encoded password: {encoded}")

    print("Fetching external data:")
    print(get_data())
