import Backbone from 'backbone';

var Playlist = Backbone.Model.extend({
	defaults: {
		name: '',
		songs: []
	}
});

export default Playlist;