(function($){
	"use strict";
	
	
	$('.nav-menu').click(function(){
		$('#bar1, #bar2, #bar3').toggleClass('change');
		/*$('#bar1').toggleClass('change');
		  $('#bar2').toggleClass('change');
		  $('#bar3').toggleClass('change'); */
		$('#sidebar-menu').toggleClass('active');
		$(this).toggleClass('active');
	})
	 
	
	// Closes responsive menu when a scroll trigger link is clicked
    $('#sidebar-menu .js-scroll-trigger').click(function() {
      $("#sidebar-menu").removeClass("active");
      $(".nav-menu").removeClass("active");
      $("#bar1 #bar2 #bar3").togglelass("change");
    });

	
    // Scroll to top button appear
    $(document).scroll(function() {
      var scrollDistance = $(this).scrollTop();
      if (scrollDistance > 100) {
        $('.scroll-to-top').fadeIn();
      } else {
        $('.scroll-to-top').fadeOut();
      }
    });

	
})(jQuery);

// Disable Google Maps scrolling
// See http://stackoverflow.com/a/25904582/1607849
// Disable scroll zooming and bind back the click event
var onMapMouseleaveHandler = function(event) {
  var that = $(this);
  that.on('click', onMapClickHandler);
  that.off('mouseleave', onMapMouseleaveHandler);
  that.find('iframe').css("pointer-events", "none");
}
var onMapClickHandler = function(event) {
  var that = $(this);
  // Disable the click handler until the user leaves the map area
  that.off('click', onMapClickHandler);
  // Enable scrolling zoom
  that.find('iframe').css("pointer-events", "auto");
  // Handle the mouse leave event
  that.on('mouseleave', onMapMouseleaveHandler);
}
// Enable map zooming with mouse scroll when the user clicks the map
$('.map').on('click', onMapClickHandler);