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
	$("#possiblemembers").hide();
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

function listContacts() {
    var temp = {};
    temp.bye = 'yo';
    $.ajax({
        type: "GET",
        url: 'http://localhost:8081/listTeam',
        data: JSON.stringify(temp),
        contentType: "application/json; charset=utf-8",
        dataType: "json",
        success: function(data) {
            //data is the array of all the contact objects
            teammembers = data;
            var listContent = "";
            //display the objects on the webpage
            for (var i = 0; i < 3; i++) {
                listContent += "<li id=" + i + " class=\"active\" style=\"padding-bottom:10px\" onclick=\"display(this.id)\"><a style=\"background-color:black\">" + contactList[i].name + "</a></li> ";
            }
            $("#list").html(listContent);
        },
        error: function(msg, url, line) {
            alert('error trapped in error: function(msg, url, line)');
            alert('msg = ' + msg + ', url = ' + url + ', line = ' + line);

        }
    });
}