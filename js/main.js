index=1;

function register() {
	window.open("https://docs.google.com/forms/d/e/1FAIpQLSfcYpR6AheO2dgQAW0D1CrW8yor6RlQE95S56XKcoOPFjOR_g/viewform?c=0&w=1&usp=mail_form_link", "_blank")
}

function openMain() {
	window.open("main.html", "_self");
}

function hideAll(){
	$("#menu").hide();
	$("#page1").hide();
	$("#page2").hide();
	$("#page3").hide();
	$("#page4").hide();
}

function begin(){
	openOne();

}
function openOne(){
	hideAll();
	$("#menu").show();
	$("#page1").fadeIn(1000);
	index=1;
}

function openTwo(){
	hideAll();
	$("#menu").show();
	$("#page2").fadeIn(1000);
	index=2;
}

function openThree(){
	hideAll();
	$("#menu").show();
	$("#page3").fadeIn(1000);
	index=3;
}

function openFour(){
	hideAll();
	$("#menu").show();
	$("#page4").fadeIn(1000);
	index=4
}

document.onkeydown = checkKey;

function checkKey(e) {

    e = e || window.event;
    if (e.keyCode == '37') {
       // left arrow
       if((index-1)<1){

       }else{
     	    index--;
	        hideAll();
	     	$("#menu").show();

			$("#page"+index).fadeIn(1000);
		}
    }
    else if (e.keyCode == '39') {
       // right arrow
       if((index+1)>7){

       }else{
     	    index++;
	        hideAll();
	     	$("#menu").show();

			$("#page"+index).fadeIn(1000);
		}
    }

}