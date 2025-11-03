function concat(string_list) {
    let rstring = "";
    for (i = 0; i < string_list.length; i++) {
        rstring = rstring + string_list[i];
    }
    return rstring;
}
input = ["ben", "oijoi", "gaming"]
let output = concat(input);
document.querySelector('#target1').innerHTML = ""+output;