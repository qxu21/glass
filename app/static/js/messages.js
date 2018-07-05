//this is the first line of javascript ever written in Mutual Assured Destruction. For posterity, it shall never be deleted.

function expandMessage(event) {
    var message = this.nextElementSibling; //hopefully i can modify this
    if (message.style.display === "none") {
        //message.setAttribute("style", "");
        message.style.display = "";
    } else {
        //message.setAttribute("display", "none");
        message.style.display = "none";
    }
}

window.onload = function() {
    var trs = document.querySelectorAll(".messageheader")
    for (var tr of trs) { //var x in y would be "0" "1" "2"...
        tr.onclick = expandMessage;
        tr.nextElementSibling.style.display = "none";
    }
}
