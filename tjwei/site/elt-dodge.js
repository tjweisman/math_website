var skitteringEnabled = false;

$(document).ready(function () {
	$(".navbar li").mouseover(function (evt) {
		if(!skitteringEnabled) {
			return;
		}
		
		var distance = 100;
		var angle = Math.random() * Math.PI / 2;
		
		var dx = Math.floor(distance * Math.cos(angle));
		var dy = Math.floor(distance * Math.sin(angle));

		var h_dist = "+=" + dx + "px";
		var v_dist = "+=" + dy + "px";

		if(Math.random() > .5) {
			h_dist = "-=" + dx + "px";
		}
		if(Math.random() > .5) {
			v_dist = "-=" + dy + "px";
		}

		$(evt.currentTarget).animate({
			left : h_dist,
			top: v_dist
		},
		100);
	});
});

