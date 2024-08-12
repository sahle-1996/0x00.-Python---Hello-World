$(function () {
  $.getJSON('https://swapi.co/api/films/?format=json', function (response) {
    response.results.forEach(function (movie) {
      $('<li>').text(movie.title).appendTo('ul#list_movies');
    });
  });
});
