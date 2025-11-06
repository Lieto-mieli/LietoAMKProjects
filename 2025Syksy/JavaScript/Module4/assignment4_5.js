'use strict';
const tvform = document.querySelector('#source')
tvform.addEventListener('submit', async function (evt) {
    evt.preventDefault();
    document.getElementById("result").innerHTML = '';
    const response = await fetch(`https://api.chucknorris.io/jokes/random`);
    //const response = await fetch(`https://api.chucknorris.io/jokes/search?query=${value_from_input}`);
    const json = await response.json();
        let newart = document.createElement("article");

        let joke = document.createElement("p");
        joke.textContent = json.value;
        newart.appendChild(joke);

        document.getElementById("result").appendChild(newart);
});