let vuosi = parseInt(prompt("anna vuosi:"))
let output;
if (vuosi % 100 == 0) {
    if (vuosi % 400 == 0) {
        output = "vuotesi on karkausvuosi"
    }
    else {
        output = "vuotesi ei ole karkausvuosi"
    }
}
else if (vuosi % 4 == 0) {
    output = "vuotesi on karkausvuosi"
}
else {
    output = "vuotesi ei ole karkausvuosi"
}
document.querySelector('#target').innerHTML = output;