var express = require('express');
var app = express();
var db = require('./controllers');
app.set('port', (process.env.PORT || 5000));

// make express look in the public directory for assets (css/js/img)
app.use(express.static(__dirname + '/public'));

// might have to change these setting to match backbone
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

app.get('/', function(request, response) {
	response.render('pages/index', {index: true, profile: false});
});
app.get('/db/addRecord', function(req,res){
    db.addRecord(req,res);
});

app.get('/db/createTable', function(req,res){
    db.createTable(req,res);
});


app.get('/profile', function(request, response) {
	response.render('pages/profile', {index: false, profile: true});
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

app.get('/playlists', function(request, response) {
	// I stuck some dummy data in here, but this is the general format of
	// what this route should return.
	// Obviously this will be user-specific eventually
	response.send([
		{
			name: 'Test Playlist 1',
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
		},
		{
			name: 'Test Playlist 2',
			songs: [
				{
					name: 'Take On Me',
					artist: 'a-ha'
				},
				{
					name: 'Forever Young',
					artist: 'Alphaville'
				},
				{
					name: 'Billie Jean',
					artist: 'Michael Jackson'
				}
			]
		}
	]);
	//change this to set homepage
  response.render('pages/index');
});

app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});

exports.app = app;