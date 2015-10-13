import Backbone from 'backbone';
import _ from 'lodash';

var PlaylistView = Backbone.View.extend({
	events: {
		'click': 'collapse'
	},

	collapse: function() {
		console.log('yes');
		this.$('.panel-collapse').collapse('toggle');
	},

	getTableBody: function() {
		return _.map(this.model.songs, (song, index) => {
			return `
				<tr>
					<td>${index + 1}</td>
					<td>${song.name}</td>
					<td>${song.artist}</td>
				</tr>`;
		}).join('');
	},

	render: function() {
		this.$el.html(`
			<div class="panel panel-default">
				<div class="panel-heading">${this.model.name}</div>
				<div class="panel-collapse collapse in">
					<div class="panel-body">
						<table class="table table-hover ">
							<thead>
								<tr>
							    <th>#</th>
							    <th>Song</th>
							    <th>Artist</th>
						    	</tr>
							</thead>
							<tbody>
								${this.getTableBody()}
							</tbody>
						</table> 
					</div>
				</div>
			</div>
		`.trim());
	}
});

export default PlaylistView