let vStart = parseInt(prompt("anna vuosi josta lista aloitetaan:"))
let vEnd = parseInt(prompt("anna vuosi johon lista loppuu:"))
const output = [];
for (let vuosi = vStart; vuosi <= vEnd; vuosi++) {
    if (vuosi % 100 == 0) {
        if (vuosi % 400 == 0) {
            output.push(vuosi)
        }
        else {
            //nothing
        }
    }
    else if (vuosi % 4 == 0) {
        output.push(vuosi)
    }
    else {
        //nothing, again
    }
}
output.forEach((year) => {
    let newli = document.createElement("li");
    let newtext = document.createTextNode('' + year);
    newli.appendChild(newtext);
    document.body.insertBefore(newli, document.getElementById("target"));
})