import Playlists from '../../models/backbone/playlists.js';
import PlaylistsView from './playlists.js';

$(document).ready(() => {
	var playlists = new Playlists();

	// PlaylistsView will render itself in the right spot when it's ready
	var playlistsView = new PlaylistsView({collection: playlists});
});