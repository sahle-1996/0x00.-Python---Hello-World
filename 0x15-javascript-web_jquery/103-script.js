$(function () {
  const fetchTranslation = () => {
    $('#hello').html('');
    const language = $('#language_code').val();
    $.get(`https://fourtonfish.com/hellosalut/?lang=${language}`, (response) => {
      $('#hello').text(response.hello);
    });
  };

  $('#btn_translate').on('click', fetchTranslation);
  
  $('#language_code').on('keypress', (e) => {
    if (e.key === 'Enter') {
      fetchTranslation();
    }
  });
});
