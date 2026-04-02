//exs1 scope
// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}
// #1.1 Prediction: 3. 
// Explanation: 'a' is initialized as 5. The if-statement condition (5 > 1) is true, 
// so 'a' is reassigned to 3.

// #1.2 What happens with const?
// Prediction: TypeError. 
// Explanation: You cannot reassign a value to a variable declared with const. 
// The line 'a = 3' would throw an error.

//#2
let  = 0;
function funcTwo() {
    a = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}

// #2.1 Prediction: 
// First call to funcThree(): 0 (uses the global value).
// After funcTwo(): 5 (funcTwo reassigns the global 'a').
// Second call to funcThree(): 5.

// #2.2 What happens with const?
// Prediction: TypeError in funcTwo.
// Explanation: Since 'a' is global const, funcTwo cannot change its value.

//#3
function funcFour() {
    window.a = "hello";
}

function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

// #3.1 Prediction: "hello"
// Explanation: funcFour adds 'a' to the window object (global scope). 
// funcFive can access it.

//#4
let  = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}

// #4.1 Prediction: "test"
// Explanation: This is "shadowing." The local 'a' inside the function 
// takes precedence over the global 'a'.

// #4.2 What happens with const?
// Prediction: Still "test". 
// Explanation: You are declaring a *new* block-scoped constant, 
// not reassigning the global one.

//#5
let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);

// #5.1 Prediction: 
// Alert 1: 5 (local block scope)
// Alert 2: 2 (global scope)

// #5.2 What happens with const?
// Prediction: Same result (5 then 2). 
// Explanation: let and const both have block scope.

//exs2 
const winBattle = () => true;

let experiencePoints = winBattle() ? 10 : 1;

console.log(experiencePoints);

//exs3
const isString = (val) => typeof val === 'string';

console.log(isString('hello')); // true
console.log(isString([1, 2, 4, 0])); // false

//exs4
const sum = (a, b) => a + b;

//exs5
// Function Declaration (Hoisted)
function convertToGrams(kg) {
    return kg * 1000;
}
console.log(convertToGrams(2));

// Function Expression (Not Hoisted)
const convertToGramsExp = function(kg) {
    return kg * 1000;
};
console.log(convertToGramsExp(2));

// Difference: Function declarations are hoisted (can be called before they are defined), while function expressions are not.

// Arrow Function
const convertToGramsArrow = (kg) => kg * 1000;
console.log(convertToGramsArrow(2));

//exs6
(function(numKids, partner, location, job) {
    const sentence = `You will be a ${job} in ${location}, and married to ${partner} with ${numKids} kids.`;
    document.body.innerHTML += `<p>${sentence}</p>`;
})(3, "Taylor", "Paris", "Software Architect");

//exs7
// Make sure you have <nav id="navbar"></nav> in your HTML
(function(userName) {
    const nav = document.getElementById('navbar');
    const userDiv = document.createElement('div');
    userDiv.innerHTML = `
        <span>Welcome, ${userName}</span>
        <img src="https://via.placeholder.com/50" alt="profile" style="border-radius: 50%">
    `;
    nav.appendChild(userDiv);
})("John");

//exs8
function makeJuice(size) {
    const ingredients = [];

    function addIngredients(ing1, ing2, ing3) {
        ingredients.push(ing1, ing2, ing3);
    }

    function displayJuice() {
        const sentence = `The client wants a ${size} juice, containing ${ingredients.join(", ")}.`;
        document.body.innerHTML += `<p>${sentence}</p>`;
    }

    addIngredients("Apple", "Ginger", "Lemon");
    addIngredients("Carrot", "Beetroot", "Mint");
    displayJuice();
}

makeJuice("large");