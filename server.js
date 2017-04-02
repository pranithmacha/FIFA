var http = require('http');
var cookieParser = require('cookie-parser');
var session = require('express-session');
var express = require('express');
var bodyParser= require('body-parser');
var path = require('path');
var options, app;
app = module.exports = express();
/**
 * Get port from environment and store in Express.
 */

var port = 3000 ;
app.set('port', port);
app.use(express.static(__dirname));
/**
 * Create HTTP server.
 */
app.get('/', function(req, res) {
    res.sendFile(path.join(__dirname + '/templates/home.html'));
});
var server = http.createServer(app);

server.listen(port);
console.log('3000 listening')