let num;
let output = [];
while (true) {
    num = parseInt(prompt("giv number (0 to stop)"));
    if (num != 0) {
        output.push(num);
    }
    else { break; }
}
output = output.sort(function (a, b) { return a - b }).reverse();
for (i = 0; i < output.length; i++) {
    console.log("" + output[i])
}