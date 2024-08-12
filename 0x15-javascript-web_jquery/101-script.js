$(function () {
  $('#add_item').on('click', () => {
    $('<li>Item</li>').appendTo('ul.my_list');
  });
  $('#remove_item').on('click', () => {
    $('ul.my_list li').last().remove();
  });
  $('#clear_list').on('click', () => {
    $('ul.my_list').empty();
  });
});
