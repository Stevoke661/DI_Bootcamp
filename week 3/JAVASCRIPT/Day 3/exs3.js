//exs1 select music
// 1. Display the value of the selected option
const selectElem = document.getElementById('genres');
console.log("Initial selected value:", selectElem.value);

// 2. Add an additional option: <option value="classic">Classic</option>
const newOption = document.createElement('option');
newOption.value = 'classic';
newOption.textContent = 'Classic';

// 3. The newly added option should be selected by default
newOption.selected = true;

selectElem.appendChild(newOption);

// Verify the change
console.log("New selected value:", selectElem.value);

//exs2 delete color
<form>
    <select id="colorSelect">
        <option>Red</option>
        <option>Green</option>
        <option>White</option>
        <option>Black</option>
    </select>
    
</form>

//exs3 create list
const root = document.getElementById('root');
let shoppingList = [];

// 1. Create the Form and Inputs
const form = document.createElement('form');
const input = document.createElement('input');
input.setAttribute('type', 'text');
input.setAttribute('placeholder', 'Enter item...');

const addButton = document.createElement('button');
addButton.textContent = 'AddItem';
addButton.type = 'button'; // Prevents page refresh

// 2. Add ClearAll Button
const clearButton = document.createElement('button');
clearButton.textContent = 'ClearAll';
clearButton.type = 'button';

// Append elements to the DOM
form.appendChild(input);
form.appendChild(addButton);
root.appendChild(form);
root.appendChild(clearButton);

// 3. addItem Function
function addItem() {
    const value = input.value;
    if (value !== "") {
        shoppingList.push(value);
        console.log("Current List:", shoppingList);
        input.value = ""; // Clear input field
    }
}

// 4. clearAll Function
function clearAll() {
    shoppingList = [];
    console.log("List Cleared:", shoppingList);
}

// 5. Event Listeners
addButton.addEventListener('click', addItem);
clearButton.addEventListener('click', clearAll);