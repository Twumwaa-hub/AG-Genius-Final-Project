const express = require('express');
const cors = require('cors');
const app = express();

// Middleware
app.use(cors({
  origin: 'http://localhost:3000' // Your frontend URL
}));
app.use(express.json());

// Temporary user storage
let users = [];

// Registration endpoint
app.post('/register', (req, res) => {
  const { email, password } = req.body;
  
  // Basic validation
  if (!email || !password) {
    return res.status(400).json({ error: 'Email and password required' });
  }
  
  // Check if user exists
  if (users.some(user => user.email === email)) {
    return res.status(409).json({ error: 'User already exists' });
  }

  // Store user (in memory)
  users.push({ email, password });
  console.log('New user:', email);
  
  res.status(201).json({ success: true });
});

// Start server
const PORT = 3001;
app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
  console.log(`📝 Registration endpoint: POST http://localhost:${PORT}/register`);
});