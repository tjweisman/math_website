
function answer_text(data) {
	var typename = "horse";
	if(data["type"] == "frisbee") {
		typename = "frisbee team";
	}

	return data["name"] + ' is a <a href="' + data["url"] +
		'" class = "infolink">'+ typename + '</a>.';
}

$(document).ready(function () {
	var correct = 0;
	var total = 0;
	var data = fill_box();

	$(".button").click(function(evt) {
		evt.preventDefault();
		var guess = $(this).attr("id");
		total += 1;

		var anstr = answer_text(data);
		if(guess == data["type"]) {
			$("#result").html("Correct! " + anstr);
			$("#result").removeClass("incorrect").addClass("correct");
			correct += 1;
		} else if (data["type"] != "both") {
			$("#result").html("Incorrect. " + anstr);
			$("#result").removeClass("correct").addClass("incorrect");
		} else {
			$("#result").html("Correct! " + data["name"] + " is both a <a href = '"
				+ both[data["name"]]["hurl"] + "'>horse</a> and a <a href = '" +
				 both[data["name"]]["furl"] + "'>frisbee team</a>.");
			$("#result").removeClass("incorrect").addClass("correct");
			correct += 1;
		}

		$("#percentage").text("Correct: " + Math.floor(correct * 100.0 / total) + "% ("+correct +
			"/" + total + ")");

		data = fill_box();
	});

	$("#about-toggle").click(function(evt) {
		evt.preventDefault();
		$("#about-content").toggleClass("hidden");
	});
});

function randRange(max) {
	return Math.floor(Math.random() * max);
}

function fill_box() {
	var horse = (Math.random() > 0.5);
	var data;
	if(horse) {
		data = horses[randRange(horses.length)];
	} else {
		data = frisbee[randRange(frisbee.length)];
	}

	$("#namebox").text(data["name"]);
	return data;
}