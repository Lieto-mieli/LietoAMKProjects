function getRandomInt(min, max) {
    const minCeiled = Math.ceil(min);
    const maxFloored = Math.floor(max);
    return Math.floor(Math.random() * (maxFloored - minCeiled) + minCeiled);
} // thanks to 'https://developer.mozilla.org' for the code!
let outputf;
let outputr = 0;
let numOfDice = parseInt(prompt("How many dice?"));
let numOfFaces = parseInt(prompt("How many faces on each die?"));
let interest = parseInt(prompt("Which sum would you like to know the probability of?"));
let allDice = [];
let probabilities = {};
let succ = 0;
let fail = 0;
for (let i = 0; i < numOfDice; i++) {
    let newdie = {};
    for (let s = 0; s < numOfFaces; s++) {
        newdie[s] = 1 / numOfFaces;
    }
    allDice.push(newdie);
}
probabilities[0] = 1;
for (let i = 1; i < (numOfDice * numOfFaces)+1; i++) {
    probabilities[i] = 0
}
let curNums = 0
for (let d = 0; d < allDice.length; d++) {
    curDice = allDice[d];
    for (let p = curNums; p >= 0; p--) {
        for (let f = 0; f < numOfFaces; f++) {
            probabilities[p + (f + 1)] = (probabilities[p] * curDice[f]) + probabilities[p + (f + 1)];
        }
        probabilities[p] = 0;   
    }
    curNums += Object.keys(curDice).length;
}
outputf = probabilities[interest];
document.querySelector('#target1').innerHTML = (outputf * 100).toFixed(4) + '% chance for the sum of ' + numOfDice + ' d' + numOfFaces + ' to be ' + interest;
for (let s = 0; s < 10000; s++) {
    outputr = 0
    for (let i = 0; i < numOfDice; i++) {
        outputr += getRandomInt(1, numOfFaces + 1);
    }
    if (outputr == interest) {
        succ++;
    }
    else {
        fail++;
    }
}
outputr = succ/10000
document.querySelector('#target2').innerHTML = 'Test result: ' + (outputr * 100).toFixed(4) + '% chance';