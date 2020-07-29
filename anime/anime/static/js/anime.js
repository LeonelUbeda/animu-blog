var elem = document.querySelector('.featured');
var flkty = new Flickity( elem, {
  // options
  cellAlign: 'left',
  contain: true
});



$(document).ready(function(){
  $('.media-item').click(function(){
    console.log('holas')
    $(this).children(".links").slideToggle(300)
  })
})
// element argument can be a selector string
//   for an individual element
// var flkty = new Flickity( '.main-carousel', {
//   // options
// });