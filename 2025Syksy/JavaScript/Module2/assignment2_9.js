function even(num_list) {
    let rnums = [];
    for (i = 0; i < num_list.length; i++) {
        if (num_list[i] % 2 == 0) {
            rnums.push(num_list[i]);
        }
    }
    return rnums;
}
input = [1,2,3,4,5,6,7,8,9]
let output = even(input);
console.log(input)
console.log(output)
document.querySelector('#target1').innerHTML = ""+output;