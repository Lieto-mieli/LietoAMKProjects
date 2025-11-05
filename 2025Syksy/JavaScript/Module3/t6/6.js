'use strict';
function alertwindow() {
    alert("Button Clicked");
}
let b = document.getElementById("target");
b.onclick = function () {alertwindow() };