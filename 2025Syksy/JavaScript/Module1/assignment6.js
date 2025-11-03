let output
if (confirm("Should I calculate the square root?")) {
    let num = parseInt(prompt("Enter a number:"))
    if (num < 0) {
        output = "The square root of a negative number is not defined"
    }
    else {
        output = Math.sqrt(num)
    }
}
else {
    output = "The square root is not calculated."
}
document.querySelector('#target').innerHTML = output;