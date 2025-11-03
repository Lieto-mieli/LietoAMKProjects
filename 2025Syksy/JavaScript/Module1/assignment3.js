'use strict';
let num1 = parseInt(prompt('Type the first integer.'));
let num2 = parseInt(prompt('Type the second integer.'));
let num3 = parseInt(prompt('Type the third integer.'));
let sum = num1 + num2 + num3
let product = num1 * num2 * num3
let average = sum / 3
document.querySelector('#target').innerHTML = 'Sum: ' + sum + ' - Product: ' + product + ' - Average: ' + average;