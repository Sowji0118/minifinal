const mongoose = require('mongoose');

// Use MONGODB_URI env var, fallback to localhost
const MONGODB_URI = process.env.MONGODB_URI || 'mongodb://127.0.0.1:27017/vidyamitra';

function connectDB() {
  return mongoose.connect(MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  }).then(() => {
    console.log('✅ MongoDB connected: ' + MONGODB_URI);
  }).catch(err => {
    console.error('MongoDB connection error:', err);
    // do not exit the process to avoid changing app flow; just log
  });
}

module.exports = connectDB;
