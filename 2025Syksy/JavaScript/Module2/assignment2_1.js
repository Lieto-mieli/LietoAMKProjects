let nums = [];
for (i = 1; i < 6; i++) {
    nums.push(parseInt(prompt("Enter a number (" + i + "/5)")));
    console.log(nums);
}
let output = [];
for (i = 4; i > -1; i--) {
    output[i] = nums[nums.length - (i+1)];
    console.log(output);
}
output.forEach((num) => {
    let newli = document.createElement("li");
    let newtext = document.createTextNode('' + num);
    newli.appendChild(newtext);
    document.body.insertBefore(newli, document.getElementById("list"));
})