var express = require('express');
var app = express();

app.set('port', (process.env.PORT || 5000));

app.use(express.static(__dirname + '/public'));

// views is directory for all template files
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

app.get('/', function(request, response) {
	response.render('pages/index');
});

app.get('/profile', function(request, response) {
	response.render('pages/profile');
});

app.get('/generate', function(request, response) {
	// I stuck some dummy data in here, but this is the general format of
	// what this route should return.
	response.send({
		name: 'Test Playlist',
		songs: [
			{
				name: 'Hotline Bling',
				artist: 'Drake'
			},
			{
				name: 'Monster',
				artist: 'Kanye West'
			},
			{
				name: 'Poetic Justice',
				artist: 'Kendrick Lamar'
			}
		]
	});
});

app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});


