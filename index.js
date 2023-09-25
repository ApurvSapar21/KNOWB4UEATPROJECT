// Require the express web application framework (https://expressjs.com)
var express = require('express');
var app = express();

// Get port from environment and store in Express.
var port = normalizePort(process.env.PORT || '3000');
app.set('port', port);

/**
 * Normalize a port into a number, string, or false.
 */
function normalizePort(val) {
  var port = parseInt(val, 10);

  if (isNaN(port)) {
    // named pipe
    return val;
  }

  if (port >= 0) {
    // port number
    return port;
  }

  return false;
}

// Tell our application to serve all the files under the `public_html` directory
app.use(express.static('public_html'))

// Route for handling barcode scanning
app.get('/scan', function (req, res) {
  // Placeholder logic for barcode scanning
  // Here you can integrate a barcode scanning library and perform the scanning process
  // For demonstration purposes, we'll simply send a response
  res.send('Scanning in progress...');
});

// Tell our application to listen to requests at port 3000 on the localhost
app.listen(port, function () {
  console.log(`Web server running at: http://localhost:${port}`)
  console.log("Type Ctrl+C to shut down the web server")
});
