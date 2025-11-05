'use strict';
function pic() {
    let im = document.getElementById("target");
    im.src = "img/picB.jpg";
}
function picleave() {
    let im = document.getElementById("target");
    im.src = "img/picA.jpg";
}
let b = document.getElementById("trigger");
b.onmouseenter = function () { pic() };
b.onmouseleave = function () { picleave() };