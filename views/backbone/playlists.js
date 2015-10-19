import Backbone from 'backbone';
import _ from 'lodash';
import PlaylistView from './playlist.js';

// Pass in a Playlists collection to create
var PlaylistsView = Backbone.View.extend({
	initialize: function() {
		this.subviews = [];

		this.collection.on('reset', () => {
			this.createSubviews();
			this.render();
		});

		this.collection.fetch({reset: true});
	},

	createSubviews: function() {
		_.each(this.collection.models, (playlist) => {
			this.subviews.push(new PlaylistView({model: playlist}));
		});
	},

	// I'm assuming this thing is only gonna render once otherwise
	// this is gonna get wayyy more complicated (or memory leaky)
	render: function() {
		var $container = $('#playlists');
		_.each(this.subviews, (subview) => {
			subview.render();
			$container.append(subview.$el);
		});
	}
});

export default PlaylistsView;