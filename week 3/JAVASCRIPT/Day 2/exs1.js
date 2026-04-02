//exs1
function displayNumbersDivisible(divisor = 23) {
    let sum = 0;
    let numbers = [];

    for (let i = 0; i <= 500; i++) {
        if (i % divisor === 0) {
            numbers.push(i);
            sum += i;
        }
    }

    console.log("Outcome:", numbers.join(" "));
    console.log("Sum:", sum);
}

displayNumbersDivisible(); // Default 23

//exs2
const stock = { "banana": 6, "apple": 0, "pear": 12, "orange": 32, "blueberry":1 };
const prices = { "banana": 4, "apple": 2, "pear": 1, "orange": 1.5, "blueberry":10 };

const shoppingList = ["banana", "orange", "apple"];

function myBill() {
    let total = 0;

    for (const item of shoppingList) {
        // Check if item exists in stock and is > 0
        if (item in stock && stock[item] > 0) {
            total += prices[item];
            stock[item] -= 1; // Bonus: decrease stock
        }
    }
    return total;
}

console.log("Total Bill:", myBill());

//exs3
function changeEnough(itemPrice, amountOfChange) {
    const quarters = amountOfChange[0] * 0.25;
    const dimes = amountOfChange[1] * 0.10;
    const nickels = amountOfChange[2] * 0.05;
    const pennies = amountOfChange[3] * 0.01;

    const totalChange = quarters + dimes + nickels + pennies;

    return totalChange >= itemPrice;
}

console.log(changeEnough(4.25, [25, 20, 5, 0])); // true

//exs4
function hotelCost() {
    let nights;
    while (isNaN(nights) || nights <= 0) {
        nights = prompt("How many nights would you like to stay?");
    }
    return nights * 140;
}

function planeRideCost() {
    let destination = "";
    while (destination === "" || !isNaN(destination)) {
        destination = prompt("Where are you going?");
    }
    
    if (destination === "London") return 183;
    if (destination === "Paris") return 220;
    return 300;
}

function rentalCarCost() {
    let days;
    while (isNaN(days) || days <= 0) {
        days = prompt("How many days for the car?");
    }
    let cost = days * 40;
    if (days > 10) cost *= 0.95; // 5% discount
    return cost;
}

function totalVacationCost() {
    const hotel = hotelCost();
    const plane = planeRideCost();
    const car = rentalCarCost();

    console.log(`The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}.`);
    return hotel + plane + car;
}

totalVacationCost();

//exs5
// 1. Retrieve the div
const container = document.getElementById('container');
console.log(container);

// 2. Change Pete to Richard
document.querySelectorAll('.list')[0].children[1].textContent = "Richard";

// 3. Delete second <li> of second <ul>
const secondUl = document.querySelectorAll('.list')[1];
secondUl.removeChild(secondUl.children[1]);

// 4. Change first <li> to your name
const allLists = document.querySelectorAll('.list');
allLists.forEach(ul => {
    ul.firstElementChild.textContent = "YourName";
});

// Classes
allLists.forEach(ul => ul.classList.add("student_list"));
allLists[0].classList.add("university", "attendance");

// Styles
container.style.backgroundColor = "lightblue";
container.style.padding = "10px";

// Hide Dan (Last <li> of first <ul>)
// Note: Instructions say last of first ul, which is now the 2nd child 
allLists[0].lastElementChild.style.display = "none";

// Border to Richard
const listItems = document.getElementsByTagName('li');
for (let li of listItems) {
    if (li.textContent === "Richard") li.style.border = "1px solid black";
}

document.body.style.fontSize = "20px";

//exs6
// Change ID
const nav = document.getElementById('navBar');
nav.setAttribute('id', 'socialNetworkNavigation');

// Add Logout
const ul = nav.querySelector('ul');
const newLi = document.createElement('li');
const textNode = document.createTextNode('Logout');
newLi.appendChild(textNode);
ul.appendChild(newLi);

// First and Last
console.log("First:", ul.firstElementChild.textContent);
console.log("Last:", ul.lastElementChild.textContent);

//exs7
const allBooks = [
    {
        title: "The Hobbit",
        author: "J.R.R. Tolkien",
        image: "https://example.com/hobbit.jpg",
        alreadyRead: true
    },
    {
        title: "1984",
        author: "George Orwell",
        image: "https://example.com/1984.jpg",
        alreadyRead: false
    }
];

const section = document.querySelector('.listBooks');

allBooks.forEach(book => {
    const div = document.createElement('div');
    const info = document.createElement('p');
    const img = document.createElement('img');

    info.textContent = `${book.title} written by ${book.author}`;
    img.src = book.image;
    img.style.width = "100px";

    if (book.alreadyRead) {
        info.style.color = "red";
    }

    div.appendChild(info);
    div.appendChild(img);
    section.appendChild(div);
});