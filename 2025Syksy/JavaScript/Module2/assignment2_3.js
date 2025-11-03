let num = 6
let output = [];
for (i = 0; i < num; i++) {
    output[i] = prompt("What is the name of dog nro. " + (i + 1) + "?");
}
output.sort().reverse();
output.forEach((participant_name) => {
    let newli = document.createElement("li");
    let newtext = document.createTextNode('' + participant_name);
    newli.appendChild(newtext);
    document.body.insertBefore(newli, document.getElementById("list"));
})