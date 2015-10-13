import _ from 'lodash';
import GeneratedPlaylistView from './generated_playlist.js';

$(document).ready(() => {
	$('#playlist-form').submit((ev) => {
		ev.preventDefault();


		$('.well').fadeOut(500, () => {
			var request = {};
			_.each($('#playlist-form').serializeArray(), (input) => {
				request[input.name] = input.value;
			});
			
			$.get('/generate', request).done((playlist) => {
				var playlistView = new GeneratedPlaylistView({model: playlist});
				playlistView.render();
				

				$('.content').html(playlistView.$el);
			});
		});
	});
});