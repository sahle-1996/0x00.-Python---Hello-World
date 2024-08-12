$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (response) {
    $('#hello').html(response.hello);
  });
});
