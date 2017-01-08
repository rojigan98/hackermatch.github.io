index = 1;

function register() {
    window.open("https://docs.google.com/forms/d/e/1FAIpQLSfcYpR6AheO2dgQAW0D1CrW8yor6RlQE95S56XKcoOPFjOR_g/viewform?c=0&w=1&usp=mail_form_link", "_blank")
}

function openMain() {
    window.open("main.html", "_self");
}

function hideAll() {
    $("#menu").hide();
    $("#page1").hide();
    $("#page2").hide();
    $("#page3").hide();
    $("#page4").hide();
}

function begin() {
    openOne();

}

function openOne() {
    hideAll();
    $("#menu").show();
    $("#page1").fadeIn(1000);
    index = 1;
}

function openTwo() {
    hideAll();
    $("#menu").show();
    $("#page2").fadeIn(1000);
    $("#possiblemembers").hide();
    index = 2;
}

function openThree() {
    hideAll();
    $("#menu").show();
    $("#page3").fadeIn(1000);
    index = 3;
}

function openFour() {
    hideAll();
    $("#menu").show();
    $("#page4").fadeIn(1000);
    index = 4
}

document.onkeydown = checkKey;

function checkKey(e) {

    e = e || window.event;
    if (e.keyCode == '37') {
        // left arrow
        if ((index - 1) < 1) {

        } else {
            index--;
            hideAll();
            $("#menu").show();

            $("#page" + index).fadeIn(1000);
        }
    } else if (e.keyCode == '39') {
        // right arrow
        if ((index + 1) > 7) {

        } else {
            index++;
            hideAll();
            $("#menu").show();

            $("#page" + index).fadeIn(1000);
        }
    }
}

function getTeam() {
    //all objects
    //var email=get email by id
    var obj;
    var targetEmail=$("#email").val();
    console.log(email);
    blockspring.runParsed("query-public-google-spreadsheet", {
        "query": "SELECT A, B, C",
        "url": "https://docs.google.com/spreadsheets/d/1ZYvcYf_41aghdXRSpg25TKW4Qj9p1Lpz92b1xG-9R1Q/edit?usp=sharing"
    }, {
        "api_key": "br_50064_1fe91fe1478ef990dc8b5e9b4041c2c476670306"
    }, function(res) {
        obj = res.params;
        console.log(obj)
        var userIndex=0;
        for (var i = 0; i < 8; i++) {
            var temp = obj.data[i];
            if(targetEmail==temp.Email){
            	userIndex=i;
            }
        }
        console.log(userIndex);
        var othermembers=[];
        var teamnumber=userIndex/4;
        var membernumber=userIndex%4;
        var indices=[0,0,0];
        var j=0;
        for(var i=0; i<3; i++){
        	if(membernumber==i){
        		j++;
        	}
        	indices[i]=j;
        	j++;
        }
        for(var i=0; i<3; i++){
        	othermembers.push(obj.data[teamnumber*4+indices[i]]);
        }
        console.log(othermembers);
    });

}
//for(int i=0; i<)