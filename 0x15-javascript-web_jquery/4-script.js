$(function () {
  $('#toggle_header').on('click', function () {
    $('header').hasClass('red') ? $('header').toggleClass('red green') : $('header').toggleClass('green red');
  });
});
