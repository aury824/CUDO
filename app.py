# filename: vulnerable_app.py

from flask import Flask, request
import sqlite3

app = Flask(__name__)

# 취약한 하드코딩 비밀번호 (Secrets detection 테스트용)
DB_PASSWORD = "supersecret123"

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # 취약한 SQL Injection (SAST 테스트용)
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor.execute(query)
    result = cursor.fetchone()
    conn.close()

    if result:
        return "Login success"
    else:
        return "Login failed"

if __name__ == '__main__':
    app.run(debug=True)
