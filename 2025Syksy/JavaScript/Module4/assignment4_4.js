'use strict';
const tvform = document.querySelector('#source')
tvform.addEventListener('submit', async function (evt) {
    evt.preventDefault();
    document.getElementById("result").innerHTML = '';
    const q = document.forms["f"]["q"].value;
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${q}`);
    const json = await response.json();
    for (let i = 0; i < json.length; i++) {
        let newart = document.createElement("article");

        let name = document.createElement("h2");
        name.textContent = json[i].show.name;
        newart.appendChild(name);

        let a = document.createElement("a");
        a.target = "_blank";
        a.text = json[i].show.url;
        newart.appendChild(a);

        let img = document.createElement("img");
        img.src = ("image" in json[i].show) ? json[i].show.image.medium : "https://placehold.co/210x295?text=Not%20Found";
        newart.appendChild(img);

        newart.innerHTML+=(json[i].show.summary);

        document.getElementById("result").appendChild(newart);
    }
});