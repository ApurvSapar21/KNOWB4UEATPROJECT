// server/routes/allergies.js
const express = require('express');
const router = express.Router();
const passport = require('passport');
const Allergy = require('../models/Allergy');

// Middleware for authentication
router.use(passport.authenticate('jwt', { session: false }));

// Get user's allergies
router.get('/', async (req, res) => {
  try {
    const allergies = await Allergy.find({ user: req.user.id });
    res.json(allergies);
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Add a new allergy
router.post('/', async (req, res) => {
  try {
    const { name } = req.body;
    const newAllergy = new Allergy({ name, user: req.user.id });
    await newAllergy.save();
    res.status(201).json({ message: 'Allergy added successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

// Delete an allergy
router.delete('/:id', async (req, res) => {
  try {
    const allergy = await Allergy.findOne({ _id: req.params.id, user: req.user.id });

    if (!allergy) {
      return res.status(404).json({ message: 'Allergy not found' });
    }

    await allergy.remove();
    res.json({ message: 'Allergy deleted successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).json({ message: 'Internal server error' });
  }
});

module.exports = router;
