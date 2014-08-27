 /**
 * This demo was prepared for you by Petr Tichy - Ihatetomatoes.net
 * Want to see more similar demos and tutorials?
 * Help by spreading the word about Ihatetomatoes blog.
 * Facebook - https://www.facebook.com/ihatetomatoesblog
 * Twitter - https://twitter.com/ihatetomatoes
 * Google+ - https://plus.google.com/u/0/109859280204979591787/about
 * Article URL: http://ihatetomatoes.net/simple-parallax-scrolling-tutorial/
 */

( function( $ ) {
	
	// Setup variables
	$window = $(window);
	$slide = $('.homeSlide');
	$body = $('body');
	
    //FadeIn all sections   
	$body.imagesLoaded( function() {
		setTimeout(function() {
		      
		      // Resize sections
		      adjustWindow();
		      
		      // Fade in sections
			  $body.removeClass('loading').addClass('loaded');
			  
		}, 800);
	});
	
	function adjustWindow(){
		
		// Init Skrollr
		
		
		// Get window size
	    winH = $window.height();
	    
	    // Keep minimum height 550
	    if(winH <= 550) {
			winH = 550;
		} 
	    
	    // Resize our slides
	    $slide.height(winH);
	    
	    // Refresh Skrollr after resizing our sections
	    
	    
	}

    $.ajax({
        url:'https://api.instagram.com/v1/users/self/media/recent?count=6&access_token=422016425.1fb234f.c3920193f58a43dd9ac36e8e6cfafd16',
        type:'GET',
        dataType:'jsonp',
        success: function(response){
            console.log(response);
            len = response.data;
            for(var i =0; i < len.length; i++){
                src = response.data[i].images.low_resolution.url;
                $(".igpics").append("<img style='padding: 7px; width: 200px;' src='"+src+"'/>");
            }
        }

    });


		
} )( jQuery );