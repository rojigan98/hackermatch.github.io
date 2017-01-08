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
    $("#hider").show();
    hideAll();
    $("#menu").show();
    $("#page1").fadeIn(2000);
    $("#hider").fadeOut(1000);
    index = 1;

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
    $("#errormessage").html("")
    //all objects
    //var email=get email by id
    var obj;
    var numPeople=0;
    var targetEmail = $("#email").val();
    console.log(email);
    blockspring.runParsed("query-public-google-spreadsheet", {
        "query": "SELECT B, C, D, H, I, J, L where L>0 order by L ",
        "url": "https://docs.google.com/spreadsheets/d/1GH7WE6mUHlc-wH5BGLVIH8zz3CjnSTf3Mx-MHLzr-Jc/edit?usp=sharing"
    }, {
        "api_key": "br_50064_1fe91fe1478ef990dc8b5e9b4041c2c476670306"
    }, function(res) {
    	obj = res.params;
        console.log(obj);
        var userIndex = -1;
        for (var i = 0; i < 16; i++) {
            var temp = obj.data[i];
            if (targetEmail == temp.Email) {
                userIndex = i;
            }
        }
        console.log(userIndex);
        if (userIndex != -1) {
            var othermembers = [];
            var teamnumber = Math.floor(userIndex / 4);
            var membernumber = userIndex % 4;
            var indices = [0, 0, 0];
            var j = 0;
            for (var i = 0; i < 3; i++) {
                if (membernumber == i) {
                    j++;
                }
                indices[i] = j;
                j++;
            }
            for (var i = 0; i < 3; i++) {
            	console.log(teamnumber*4+indices[i])
                othermembers.push(obj.data[teamnumber * 4 + indices[i]]);
            }
            console.log(othermembers);
            var tempname, tempemail;

            for (var i = 1; i < 4; i++) {
                $("#" + i + "name").html("<center>" + othermembers[i - 1].Name + "</center>");
                $("#" + i + "email").html("<center>" + othermembers[i - 1].Email + "</center>");
                $("#" + i + "language").html("<center>" + othermembers[i - 1].LanguagesKnown + "</center>");
                $("#" + i + "university").html("<center>" + othermembers[i - 1].University + "</center>");
                $("#" + i + "typeHack").html("<center>" + othermembers[i - 1].TypeOfHack + "</center>");
                $("#" + i + "focus").html("<center>" + othermembers[i - 1].Focus + "</center>");
            }
        } else {
            $("#errormessage").html("<br/>Unable to find your team (you either opted out of team matching, did not register, or were not accepted).");
        }

    });

}