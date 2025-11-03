let output;
let num = parseInt(prompt("Which number to check as prime?"));
const jaolliset = [];
let onAlkuluku = true
for (let i = 2; i < num; i++) {
    if (num % i == 0) {
        onAlkuluku = false;
        jaolliset.push(i);
    }
}
if (onAlkuluku) {
    output = num + " is a prime number.";
}
else {
    output = num + " is not a prime number, because it is divisible by these whole numbers:";
    jaolliset.forEach((dnum) => {
        let newli = document.createElement("li");
        let newtext = document.createTextNode('' + dnum);
        newli.appendChild(newtext);
        document.body.insertBefore(newli, document.getElementById("list"));
    })
}
document.querySelector('#target').innerHTML = '' + output;