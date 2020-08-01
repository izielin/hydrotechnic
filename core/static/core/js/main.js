setTimeout(function() {
$(document).ready(function() {

	let counters = $(".count");
	let countersQuantity = counters.length;
	let counter = [];

	for (i = 0; i < countersQuantity; i++) {
	  counter[i] = parseInt(counters[i].innerHTML);
	}


	let count = function(start, value, id) {
	  let localStart = start;
	  setInterval(function() {
		if (localStart < value) {
		  localStart++;
		  counters[id].innerHTML = localStart;
		}
	  }, 60);
	}


	for (j = 0; j < countersQuantity; j++) {
	  count(0, counter[j], j);
	}
  });

}, 5700);


let owl = $('.owl-carousel');
owl.owlCarousel({
    items:1,
    loop:true,
    margin:10,
    autoplay:true,
    autoplayTimeout:20000,
    autoplayHoverPause:true
});


