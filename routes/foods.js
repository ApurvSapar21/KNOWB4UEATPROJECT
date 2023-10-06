// server/routes/foods.js
const express = require('express');
const router = express.Router();
const passport = require('passport');



// Middleware for authentication
router.use(passport.authenticate('jwt', { session: false }));

// Add your barcode scanning logic here
router.post('/scan', async (req, res) => {
  try {
    const { barcode } = req.body;
    // Fetch information about the scanned food item and its ingredients
    // Compare ingredients with the user's allergies
    // If allergen found, set an allergenAlert message
    // If no allergen found, set allergenAlert as an empty string

    const allergenAlert = ''; // Set this based on your logic

    res.json({ allergenAlert });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

module.exports = router;
