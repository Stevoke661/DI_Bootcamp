//exs1
// 1. Retrieve the h1 and console.log it
const h1 = document.querySelector('article h1');
console.log(h1);

// 2. Remove the last paragraph in the <article> tag
const article = document.querySelector('article');
article.lastElementChild.remove();

// 3. Change h2 background to red on click
const h2 = document.querySelector('h2');
h2.addEventListener('click', () => {
    h2.style.backgroundColor = 'red';
});

// 4. Hide h3 when clicked
const h3 = document.querySelector('h3');
h3.addEventListener('click', () => {
    h3.style.display = 'none';
});

// 5. Add button to make all paragraphs bold
const btn = document.createElement('button');
btn.textContent = 'Make Bold';
document.body.appendChild(btn);

btn.addEventListener('click', () => {
    const paragraphs = document.querySelectorAll('p');
    paragraphs.forEach(p => p.style.fontWeight = 'bold');
});

// BONUS 1: Random h1 font size on hover
h1.addEventListener('mouseover', () => {
    const randomSize = Math.floor(Math.random() * 101);
    h1.style.fontSize = `${randomSize}px`;
});

// BONUS 2: Fade out 2nd paragraph on hover
const secondP = document.querySelectorAll('p')[1];
secondP.addEventListener('mouseover', () => {
    secondP.style.transition = 'opacity 1s';
    secondP.style.opacity = '0';
});

//exs2
// 1. Retrieve the form
const form = document.querySelector('form');
console.log(form);

// 2. Retrieve inputs by ID
const fnameInput = document.getElementById('fname');
const lnameInput = document.getElementById('lname');
console.log(fnameInput, lnameInput);

// 3. Retrieve inputs by name attribute
const fnameByName = document.getElementsByName('firstname')[0];
const lnameByName = document.getElementsByName('lastname')[0];
console.log(fnameByName, lnameByName);

// 4. Submit Event
form.addEventListener('submit', (e) => {
    // Why preventDefault? To stop the page from refreshing 
    // and losing the data before we can process it.
    e.preventDefault();

    const fValue = fnameInput.value.trim();
    const lValue = lnameInput.value.trim();

    if (fValue !== "" && lValue !== "") {
        const ul = document.querySelector('.usersAnswer');
        
        const liFirst = document.createElement('li');
        liFirst.textContent = fValue;
        
        const liLast = document.createElement('li');
        liLast.textContent = lValue;

        ul.appendChild(liFirst);
        ul.appendChild(liLast);
    }
});

//exs3
// 1. Global variable
let allBoldItems;

// 2. Function to collect bold items
function getBoldItems() {
    allBoldItems = document.querySelectorAll('strong');
}

// 3. Function to highlight blue
function highlight() {
    getBoldItems(); // Ensure we have the items
    allBoldItems.forEach(item => item.style.color = 'blue');
}

// 4. Function to return to black
function returnItemsToDefault() {
    allBoldItems.forEach(item => item.style.color = 'black');
}

// 5. Event Listeners
const paragraph = document.querySelector('p');
paragraph.addEventListener('mouseover', highlight);
paragraph.addEventListener('mouseout', returnItemsToDefault);

//exs4
const sphereForm = document.getElementById('MyForm');

sphereForm.addEventListener('submit', (e) => {
    e.preventDefault();
    
    const radius = parseFloat(document.getElementById('radius').value);
    const volumeField = document.getElementById('volume');

    if (!isNaN(radius)) {
        // Calculation: (4/3) * PI * r cubed
        const volume = (4 / 3) * Math.PI * Math.pow(radius, 3);
        
        // Display result fixed to 2 decimal places
        volumeField.value = volume.toFixed(2);
    } else {
        alert("Please enter a valid number for the radius.");
    }
});