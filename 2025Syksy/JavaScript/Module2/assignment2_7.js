function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
} // thanks to 'https://developer.mozilla.org' for the code!
function d6roll(sides) {
    return getRandomInt(1, sides+1);
}
let output = [];
sides = parseInt(prompt("How many sides do you want in your die?"));
while (true) {
    num = d6roll(sides);
    output.push(num)
    if (num==sides) { break; }
}
output.forEach((participant_name) => {
    let newli = document.createElement("li");
    let newtext = document.createTextNode('' + participant_name);
    newli.appendChild(newtext);
    document.body.insertBefore(newli, document.getElementById("list"));
})