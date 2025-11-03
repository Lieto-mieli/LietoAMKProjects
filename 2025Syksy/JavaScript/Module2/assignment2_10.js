let num1 = parseInt(prompt("How many candidates?"));
let input = [];
for (i = 0; i < num1; i++) {
    input[i] = { "name": "", "votes": 0 };
    input[i].name = prompt("Name for candidate " + (i + 1));
}
num2 = parseInt(prompt("How many voters?"));
let votes = [];
for (i = 0; i < num2; i++) {
    vote = prompt("Voter " + (i + 1) + ". Name the candidate you wish to vote for.");
    for (c = 0; c < num1; c++) {
        if (input[c].name.toLowerCase() == vote.toLowerCase()) {
            input[c].votes++;
        }
    }
}
input = input.sort(function (a, b) { return a.votes - b.votes }).reverse();
document.querySelector('#target1').innerHTML = "The winner is " + input[0].name + " with " + input[0].votes + " votes.";
console.log("The winner is " + input[0].name + " with " + input[0].votes + " votes.")
document.querySelector('#target2').innerHTML = "results:";
console.log("results:")
input.forEach((candidate) => {
    let newli = document.createElement("li");
    let newtext = document.createTextNode('' + candidate.name + ": " + candidate.votes + " votes");
    console.log(candidate.name + ": " + candidate.votes + " votes")
    newli.appendChild(newtext);
    document.body.insertBefore(newli, document.getElementById("list"));
})