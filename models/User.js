// server/models/User.js
const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  username: String,
  email: String,
  password: String,
  allergies: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Allergy' }],
});

module.exports = mongoose.model('User', userSchema);
