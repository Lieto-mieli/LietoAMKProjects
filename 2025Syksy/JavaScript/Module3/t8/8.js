'use strict';
function calc() {
    let num1 = parseInt(document.getElementById("num1").value);
    let num2 = parseInt(document.getElementById("num2").value);
    if (op.value == "add") {
        return num1 + num2;
    }
    if (op.value == "sub") {
        return num1 - num2;
    }
    if (op.value == "multi") {
        return num1 * num2;
    }
    if (op.value == "div") {
        return num1 / num2;
    }
}
let op = document.getElementById("operation");
let b = document.getElementById("start");
b.onclick = function () { document.getElementById("result").textContent = calc() };