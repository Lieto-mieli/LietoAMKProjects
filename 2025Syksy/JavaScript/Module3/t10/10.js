'use strict';
function form() {
    
    let fn = document.forms["f"]["firstname"].value;
    let ln = document.forms["f"]["lastname"].value;
    return "Your name is " + fn + " " + ln;
}
let f = document.getElementById("source");
f.action = "/action_page.php";
f.onsubmit = function () { document.getElementById("target").textContent = form() };