const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());
app.use(express.json());

app.use('/posts', require('./routes/posts'));

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
