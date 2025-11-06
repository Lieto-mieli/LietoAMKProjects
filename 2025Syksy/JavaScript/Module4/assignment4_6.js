'use strict';
const tvform = document.querySelector('#source')
tvform.addEventListener('submit', async function (evt) {
    evt.preventDefault();
    document.getElementById("result").innerHTML = '';
    const q = document.forms["f"]["q"].value;
    const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${q}`);
    const json = await response.json();
    console.log(json);
    let newart = document.createElement("article");

    let joke = document.createElement("p");
    joke.textContent = (json.result.length > 0) ? json.result[0].value : "No joke found :((";
    newart.appendChild(joke);

    document.getElementById("result").appendChild(newart);
});