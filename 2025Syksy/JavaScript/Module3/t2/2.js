let target = document.getElementById('target');
input = ["First item", "Second item", "Third item"];
input.forEach((item) => {
    let newli = document.createElement("li");
    let newtext = document.createTextNode('' + item);
    newli.appendChild(newtext);
    if (item == "Second item") {
        newli.className = "my-item";
    }
    document.body.insertBefore(newli, target);
})