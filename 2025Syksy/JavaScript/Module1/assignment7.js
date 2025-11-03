function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
} // thanks to 'https://developer.mozilla.org' for the code!
let output = 0;
let num = parseInt(prompt("How many dice to roll? (d6):"));
for (let i = 0; i < num; i++) {
    output += getRandomInt(1, 7);
}
document.querySelector('#target').innerHTML = 'Sum of dice: ' + output;