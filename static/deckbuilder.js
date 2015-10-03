(function() {

	var DIMENSION = 4;
	var height = "400px";
	var width = "300px";

	var deck = [];
	var deckname = "";

	window.onload = function() {
		makeGrid();
		makeCounter();
		var cards = document.querySelectorAll('.card');
		for (var i = 0; i < cards.length; i++) {
			cards[i].onclick = addCard;
		}
		var heroinput = document.getElementById('class');
		var url = window.location.href.split("/");
		var hero = url[url.length-1];
		heroinput.value = hero;
		//cleanList();
		//document.getElementById("savenamebutton").onclick = saveDeck;
	}

	function saveDeck() {
		var deckname = document.getElementById("deckname").value;
		deck.unshift(deckname);
		$.ajax({
			type: 'POST',
			url: "{{url_for('/savedeck/')}}",
			data: JSON.stringify(deck),
			contentType: 'application/json;charset=UTF-8',
		});
	}

//	window.onbeforeunload = function() {
//		$.post("/savedeck", {
//			deck: JSON.stringify(deck)
//		});
//	}

	function makeGrid() {
		var cards = document.querySelectorAll('#cardarea div');
		for (var i = 0; i < cards.length; i++) {
			var left = i % DIMENSION * 400;
			var top = parseInt(i / DIMENSION) * 500;
			cards[i].style.left = left + "px";
			cards[i].style.top = top + "px";
		}
	}

	function makeCounter() {
		var counter = document.getElementById("counter");
		var count = deck.length;
		counter.innerHTML = "Cards: " + count + "/30";
	}

	function addCard() {
		add(this);
	}

	function add(card) {
		var name = card.querySelector('img').alt;
		deck.push(name);
		updateList(card);
		makeCounter();
	}

	//this might be redundant
	function updateList(card) {
		var container = document.getElementById("actualdeck");
		var input = document.createElement("input");

		var del = document.createElement("a");
		var linkText = document.createTextNode("Delete");
		del.appendChild(linkText);
		del.href="#";
		del.onclick = deleteCard;

		input.type = "text";
		input.name = "card"
		var name = card.querySelector('img').alt;
		input.value = name;
		container.appendChild(del);
		del.appendChild(input);
		container.appendChild(document.createElement("br"));	
	}

	function deleteCard() {
		del(this);
	}

	function del(card) {
		var parent = card.children[0];
		var name = parent.value.trim();
		var index = 0;
		for (var i = 0; i < deck.length; i++) {
			if (deck[i] === name) {
				index = i;
			}
		}
		deck.splice(index, 1);
		cleanList();
		makeCounter();
	}

	function cleanList() {
		container = document.getElementById("actualdeck");
		container.innerHTML = "";
		for (var i = 0; i < deck.length; i++) {
			var input = document.createElement("input");

			var del = document.createElement("a");
			var linkText = document.createTextNode("Delete");
			del.appendChild(linkText);
			del.href="#";
			del.onclick = deleteCard;

			var name = deck[i];
			input.value = name;
			container.appendChild(del);
			del.appendChild(input);
			container.appendChild(document.createElement("br"));
		}
	}



})();