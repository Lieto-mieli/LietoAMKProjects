'use strict';
const tvform = document.querySelector('#source')
tvform.addEventListener('submit', async function (evt) {
    evt.preventDefault();
    const q = document.forms["f"]["q"].value;
    const response = await fetch(`https://api.tvmaze.com/search/shows?q=${q}`);
    const json = await response.json();
    console.log(json); 
    //document.getElementById("result").textContent = tv(q);
});