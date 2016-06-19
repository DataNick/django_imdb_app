var Movie = Backbone.Model.extend({
  defaults: {
    title: "The Bourne Identity",
    actors: "None",
    plot: "A renegade spy out for the truth.",
    rating: "PG-13",
    poster: "None"
  },

  validate: function(attrs){
    if (attrs.age < 0){
      return "Age must be a positive number.";
    }

    if (! attrs.title){
      return 'Name can\'t be blank.'
    }
  },

  working: function(attr){
    attr.on('invalid', function(model, error){
      console.log(error);
    });
  }

});

var MovieView = Backbone.View.extend({
  tagName: 'div',
  template: _.template($('#movieTemplate').html()),
  className: 'movie',
  id: 'some-movie',
  initialize: function(){
    this.render();
  },
  render: function(){
    this.$el.html( this.template(this.model.toJSON()) );
  }
});

var movie = new Movie;
var movieview = new MovieView({ model: movie });

// $(function() {
//   new MovieView();
//  });