// server/server.js
const express = require('express');
const mongoose = require('mongoose');
const passport = require('passport');
const cors = require('cors');
const bodyParser = require('body-parser');
const keys = require('./config/keys'); // Replace with your actual configuration file
const User = require('./models/User'); // Import the 'User' model
const app = express();
const port = process.env.PORT || 5000;


// Use Passport middleware to protect a route
app.get('/protected-route', passport.authenticate('jwt', { session: false }), (req, res) => {
  // This route is protected and requires a valid JSON Web Token
  // Access user information using req.user
});
// Middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cors());

// MongoDB Configuration
//mongoose.connect(keys.mongoURI, { useNewUrlParser: true, useUnifiedTopology: true });
mongoose.connect(keys.mongoURI)
//mongoose.set('useCreateIndex', true);

// Passport Configuration
require('./config/passport')(passport);
app.use(passport.initialize());

// API Routes
const users = require('./routes/users');
const allergies = require('./routes/allergies');
const foods = require('./routes/foods');
app.use('/api/users', users);
app.use('/api/allergies', allergies);
app.use('/api/foods', foods);


// Start the server
app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
