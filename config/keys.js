// server/config/keys.js
const crypto = require('crypto');

// Generate a random secure key with 64 characters (you can adjust the length)
//const jwtSecret1 = crypto.randomBytes(32).toString('hex');
//console.log(jwtSecret1);

module.exports = {
    // MongoDB URI
    mongoURI: 'mongodb://localhost:27017/KnowB4Ueat',
       // Other configuration keys or sensitive information
       
       jwtSecret: crypto.randomBytes(32).toString('hex')
  };