'use strict';
function calc() {
    let e = document.getElementById("calculation").value;
    let l = [];
    if (e.includes("+")) {
        l = e.split("+");
        return parseInt(l[0]) + parseInt(l[1])
    }
    if (e.includes("-")) {
        l = e.split("-");
        return parseInt(l[0]) - parseInt(l[1])
    }
    if (e.includes("*")) {
        l = e.split("*");
        return parseInt(l[0]) * parseInt(l[1])
    }
    if (e.includes("/")) {
        l = e.split("/");
        return parseInt(l[0]) / parseInt(l[1])
    }
}
let b = document.getElementById("start");
b.onclick = function () { document.getElementById("result").textContent = calc() };