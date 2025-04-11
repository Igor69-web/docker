const express = require('express');
const router = express.Router();
const db = require('../db');

// Получить все посты
router.get('/', (req, res) => {
  db.query('SELECT * FROM posts', (err, results) => {
    if (err) return res.status(500).send(err);
    res.json(results);
  });
});

// Создать новый пост
router.post('/', (req, res) => {
  const { title, content } = req.body;
  db.query('INSERT INTO posts (title, content) VALUES (?, ?)', [title, content], (err, result) => {
    if (err) return res.status(500).send(err);
    res.json({ id: result.insertId, title, content });
  });
});

module.exports = router;
