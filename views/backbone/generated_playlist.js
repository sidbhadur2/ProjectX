import Backbone from 'backbone';
import PlaylistView from './playlist.js';

// A wrapper for a playlist view, to be used when we first generate a playlist
var GeneratedPlaylistView = Backbone.View.extend({
	
	className: 'generated-playlist',

	initialize: function() {
		this.playlistView = new PlaylistView({model: this.model});
	},

	render: function() {
		this.playlistView.render();
		this.$el.html(`
			<h3>Here's your new playlist:</h3>
				${this.playlistView.$el.html()}
			<button class="btn btn-info">Try Again</button>
			<button class="btn btn-primary">Save it!</button>
		`);
	}
});

export default GeneratedPlaylistView;