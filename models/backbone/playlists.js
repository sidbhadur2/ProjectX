import Backbone from 'backbone';
import Playlist from './playlist.js';

var Playlists = Backbone.Collection.extend({
	model: Playlist,
	url: '/playlists'
});

export default Playlists;