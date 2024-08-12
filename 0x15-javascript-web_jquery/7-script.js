$(function () {
  $.get('https://swapi.co/api/people/5/?format=json', function (response) {
    $('#character').html(response.name);
  });
});
