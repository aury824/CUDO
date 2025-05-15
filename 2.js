const express = require('express');
const mysql = require('mysql');
const app = express();

// ❌ 하드코딩된 비밀번호
const DB_PASSWORD = 'admin1234';

const db = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: DB_PASSWORD,
  database: "users"
});

app.use(express.urlencoded({ extended: true }));

// ❌ SQL Injection
app.post('/login', (req, res) => {
  const username = req.body.username;
  const password = req.body.password;

  const query = `SELECT * FROM users WHERE username = '${username}' AND password = '${password}'`;

  db.query(query, (err, result) => {
    if (result.length > 0) {
      res.send("Login successful");
    } else {
      res.send("Login failed");
    }
  });
});

// ❌ XSS
app.get('/welcome', (req, res) => {
  const name = req.query.name;
  res.send(`<h1>Hello, ${name}</h1>`);  // 인코딩 없음
});

app.listen(3000);
