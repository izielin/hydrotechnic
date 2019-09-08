 AOS.init({
 	duration: 800,
 	easing: 'slide'
 });

(function($) {

	"use strict";

	$(window).stellar({
    responsive: true,
    parallaxBackgrounds: true,
    parallaxElements: true,
    horizontalScrolling: false,
    hideDistantElements: false,
    scrollProperty: 'scroll'
  });


	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	// loader
	var loader = function() {
		setTimeout(function() { 
			if($('#ftco-loader').length > 0) {
				$('#ftco-loader').removeClass('show');
			}
		}, 1);
	};
	loader();




   // Burger Menu
	var burgerMenu = function() {

		$('body').on('click', '.js-fh5co-nav-toggle', function(event){

			event.preventDefault();

			if ( $('#ftco-nav').is(':visible') ) {
				$(this).removeClass('active');
			} else {
				$(this).addClass('active');	
			}

			
			
		});

	};
	burgerMenu();


	var onePageClick = function() {


		$(document).on('click', '#ftco-nav a[href^="#"]', function (event) {
	    event.preventDefault();

	    var href = $.attr(this, 'href');

	    $('html, body').animate({
	        scrollTop: $($.attr(this, 'href')).offset().top - 70
	    }, 500, function() {
	    	// window.location.hash = href;
	    });
		});

	};

	onePageClick();
	

	var carousel = function() {
		$('.carousel-testimony').owlCarousel({
			autoplay: true,
			autoHeight: true,
			center: true,
			loop: true,
			items:1,
			margin: 0,
			stagePadding: 0,
			nav: false,
			dots: true,
			navText: ['<span class="ion-ios-arrow-back">', '<span class="ion-ios-arrow-forward">'],
			responsive:{
				0:{
					items: 1
				},
				600:{
					items: 1
				},
				1000:{
					items: 1
				}
			}
		});
		$('.carousel-project').owlCarousel({
			autoplay: true,
			autoHeight: true,
			center: true,
			loop: true,
			items:1,
			margin: 30,
			stagePadding: 0,
			nav: false,
			dots: true,
			navText: ['<span class="ion-ios-arrow-back">', '<span class="ion-ios-arrow-forward">'],
			responsive:{
				0:{
					items: 1
				},
				600:{
					items: 2
				},
				1000:{
					items: 3
				}
			}
		});

	};
	carousel();

	$('nav .dropdown').hover(function(){
		var $this = $(this);
		// 	 timer;
		// clearTimeout(timer);
		$this.addClass('show');
		$this.find('> a').attr('aria-expanded', true);
		// $this.find('.dropdown-menu').addClass('animated-fast fadeInUp show');
		$this.find('.dropdown-menu').addClass('show');
	}, function(){
		var $this = $(this);
			// timer;
		// timer = setTimeout(function(){
			$this.removeClass('show');
			$this.find('> a').attr('aria-expanded', false);
			// $this.find('.dropdown-menu').removeClass('animated-fast fadeInUp show');
			$this.find('.dropdown-menu').removeClass('show');
		// }, 100);
	});


	$('#dropdown04').on('show.bs.dropdown', function () {
	  console.log('show');
	});

	// scroll
	var scrollWindow = function() {
		$(window).scroll(function(){
			var $w = $(this),
					st = $w.scrollTop(),
					navbar = $('.ftco_navbar'),
					sd = $('.js-scroll-wrap');

			if (st > 150) {
				if ( !navbar.hasClass('scrolled') ) {
					navbar.addClass('scrolled');
				}
			}
			if (st < 150) {
				if ( navbar.hasClass('scrolled') ) {
					navbar.removeClass('scrolled sleep');
				}
			}
			if ( st > 350 ) {
				if ( !navbar.hasClass('awake') ) {
					navbar.addClass('awake');
				}

				if(sd.length > 0) {
					sd.addClass('sleep');
				}
			}
			if ( st < 350 ) {
				if ( navbar.hasClass('awake') ) {
					navbar.removeClass('awake');
					navbar.addClass('sleep');
				}
				if(sd.length > 0) {
					sd.removeClass('sleep');
				}
			}
		});
	};
	scrollWindow();



})(jQuery);

 (function ($) {
	 $.fn.countTo = function (options) {
		 options = options || {};

		 return $(this).each(function () {
			 // set options for current element
			 var settings = $.extend({}, $.fn.countTo.defaults, {
				 from:            $(this).data('from'),
				 to:              $(this).data('to'),
				 speed:           $(this).data('speed'),
				 refreshInterval: $(this).data('refresh-interval'),
				 decimals:        $(this).data('decimals')
			 }, options);

			 // how many times to update the value, and how much to increment the value on each update
			 var loops = Math.ceil(settings.speed / settings.refreshInterval),
				 increment = (settings.to - settings.from) / loops;

			 // references & variables that will change with each update
			 var self = this,
				 $self = $(this),
				 loopCount = 0,
				 value = settings.from,
				 data = $self.data('countTo') || {};

			 $self.data('countTo', data);

			 // if an existing interval can be found, clear it first
			 if (data.interval) {
				 clearInterval(data.interval);
			 }
			 data.interval = setInterval(updateTimer, settings.refreshInterval);

			 // initialize the element with the starting value
			 render(value);

			 function updateTimer() {
				 value += increment;
				 loopCount++;

				 render(value);

				 if (typeof(settings.onUpdate) == 'function') {
					 settings.onUpdate.call(self, value);
				 }

				 if (loopCount >= loops) {
					 // remove the interval
					 $self.removeData('countTo');
					 clearInterval(data.interval);
					 value = settings.to;

					 if (typeof(settings.onComplete) == 'function') {
						 settings.onComplete.call(self, value);
					 }
				 }
			 }

			 function render(value) {
				 var formattedValue = settings.formatter.call(self, value, settings);
				 $self.html(formattedValue);
			 }
		 });
	 };

	 $.fn.countTo.defaults = {
		 from: 0,               // the number the element should start at
		 to: 0,                 // the number the element should end at
		 speed: 999,           // how long it should take to count between the target numbers
		 refreshInterval: 1,  // how often the element should be updated
		 decimals: 0,           // the number of decimal places to show
		 formatter: formatter,  // handler for formatting the value before rendering
	 };

	 function formatter(value, settings) {
		 return value.toFixed(settings.decimals);
	 }
 }(jQuery));

 jQuery(function ($) {

	 // start all the timers
	 $('.timer').each(count);

	 // restart a timer when a button is clicked
	 $( window ).scroll(function () {console.log($(window).scrollTop());
		 if($(window).scrollTop() > 900 && $(window).scrollTop() < 1100)
		 {
			 $('.timer').each(count);
		 }
	 });

	 function count(options) {
		 var $this = $(this);
		 options = $.extend({}, options || {}, $this.data('countToOptions') || {});
		 $this.countTo(options);
	 }
 });