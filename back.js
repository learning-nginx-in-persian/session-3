const express = require('express');
const app = express();
const PORT = 3000;

app.get('/', (req, res) => {
  res.send('Hello from the backend (Node.js app)');
});

app.listen(PORT, '127.0.0.1', () => {
  console.log(`Backend server running at http://localhost:${PORT}`);
});
