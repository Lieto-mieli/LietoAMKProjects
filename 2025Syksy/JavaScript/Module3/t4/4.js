'use strict';
const students = [
  {
    name: 'John',
    id: '2345768',
  },
  {
    name: 'Paul',
    id: '2134657',
  },
  {
    name: 'Jones',
    id: '5423679',
  },
];
for (let i = 0; i < students.length;i++) {
    let newop = document.createElement("option");
    newop.value = students[i].id;
    let newtext = document.createTextNode('' + students[i].name);
    newop.appendChild(newtext);
    document.getElementById("target").appendChild(newop);
}
