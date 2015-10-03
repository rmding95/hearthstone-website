(function() {

	var DIMENSION = 4;
	var height = "400px";
	var width = "300px";

	window.onload = function() {
		makeGrid();
	}

	function makeGrid() {
		var cards = document.querySelectorAll('#cardarea div');
		for (var i = 0; i < cards.length; i++) {
			var left = i % DIMENSION * 300;
			var top = parseInt(i / DIMENSION) * 400;
			cards[i].style.left = left + "px";
			cards[i].style.top = top + "px";
		}
	}

})();