function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
} // thanks to 'https://developer.mozilla.org' for the code!
function d6roll() {
    return getRandomInt(1, 7);
}
let output = [];
while (true) {
    num = d6roll();
    output.push(num)
    if (num==6) { break; }
}
output.forEach((participant_name) => {
    let newli = document.createElement("li");
    let newtext = document.createTextNode('' + participant_name);
    newli.appendChild(newtext);
    document.body.insertBefore(newli, document.getElementById("list"));
})