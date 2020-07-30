var elem = document.querySelector('.featured');
var flkty = new Flickity( elem, {
  // options
  cellAlign: 'left',
  contain: true
});



$(document).ready(function(){
  $('.open-links').click(function(){
    // Por el momento lo dejo asi, aunque ta bien chancho xD
    $(this).parent().parent().children(".links").slideToggle(300)

  })
})
// element argument can be a selector string
//   for an individual element
// var flkty = new Flickity( '.main-carousel', {
//   // options
// });