function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
} // thanks to 'https://developer.mozilla.org' for the code!
'use strict';
let input = prompt('What, is your name?');
let chosen = getRandomInt(1, 5);
let room;
if (chosen == 1) {
    room = "Gryffindor";
}
else if (chosen == 1) {
    room = "Slytherin";
}
else if(chosen == 1) {
    room = "Hufflepuff";
}
else {
    room = "Ravenclaw";
}
document.querySelector('#target').innerHTML = input + ', you are ' + room + '.';