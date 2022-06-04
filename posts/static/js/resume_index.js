$(window).on('scroll', function() {
  $('.upper-quarter').css('background-position', '0 -' + $(this).scrollTop() / 2 + 'px');
});