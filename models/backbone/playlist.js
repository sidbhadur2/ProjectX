import Backbone from 'backbone';

var Playlist = Backbone.Model.extend({
	defaults: {
		name: '',
		songs: []
	},

	// Delete yourself and, if you're part of a collection, make that
	// collection refetch
	deletePlaylist: function() {
		$.post('/delete');
	}
});

export default Playlist;