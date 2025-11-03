let num;
let output = [];
while (true) {
    num = parseInt(prompt("giv number"));
    if (!output.includes(num)) {
        output.push(num);
    }
    else { break; }
}
document.querySelector('#target1').innerHTML = "List already contains the number '" + num + "'";
output = output.sort(function (a, b) { return a - b });
for (i = 0; i < output.length; i++) {
    console.log("" + output[i])
}