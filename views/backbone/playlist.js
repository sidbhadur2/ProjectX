import Backbone from 'backbone';
import _ from 'lodash';
import template from '../handlebars/playlist.handlebars';
import Handlebars from 'handlebars/runtime';

// Pass in a Playlist model to create
var PlaylistView = Backbone.View.extend({
	events: {
		'click .panel-heading': 'collapse'
	},

	collapse: function() {
		$(this.el).find('.panel-collapse').collapse('toggle');
	},

	render: function() {
		Handlebars.registerHelper("inc", function(value, options)
		{
		    return parseInt(value) + 1;
		});
		this.$el.empty();
		this.$el.append(template(this.model.toJSON()));
	}
});

export default PlaylistView