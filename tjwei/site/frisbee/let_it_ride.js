$(function() {
	$("#50.strategy_table").removeClass("hidden");
	$("#possession_prob").on("change", (e) => {
		let selected = $("option:selected", this);
		$(".strategy_table").addClass("hidden");
		$("#" + selected.val() + ".strategy_table").removeClass("hidden");
	});
});