$(function () {
  $('#btn_translate').on('click', () => {
    $('#hello').html('');
    const langCode = $('#language_code').val();
    $.get(`https://fourtonfish.com/hellosalut/?lang=${langCode}`, (response) => {
      $('#hello').text(response.hello);
    });
  });
});
