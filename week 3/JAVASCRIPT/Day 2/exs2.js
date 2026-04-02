//exs1
function isBlank(str) {
    return str.length === 0;
}

console.log(isBlank(''));    // true
console.log(isBlank('abc')); // false

//exs2
function abbrevName(name) {
    const names = name.trim().split(" ");
    if (names.length > 1) {
        return `${names[0]} ${names[1].charAt(0)}.`;
    }
    return names[0];
}

console.log(abbrevName("Robin Singh")); // "Robin S."

//exs3
function swapCase(str) {
    let swapped = "";
    for (let char of str) {
        if (char === char.toUpperCase()) {
            swapped += char.toLowerCase();
        } else {
            swapped += char.toUpperCase();
        }
    }
    return swapped;
}

console.log(swapCase('The Quick Brown Fox')); // 'tHE qUICK bROWN fOX'

//exs4
function isOmnipresent(arr, val) {
    // Check if every sub-array includes the value
    return arr.every(subArr => subArr.includes(val));
}

console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 1)); // true
console.log(isOmnipresent([[1, 1], [1, 3], [5, 1], [6, 1]], 6)); // false

//exs5
let table = document.body.firstElementChild;

// Loop through the rows
for (let i = 0; i < table.rows.length; i++) {
    // Access the cell where the row index matches the column index
    // table.rows[0].cells[0], table.rows[1].cells[1], etc.
    let diagonalCell = table.rows[i].cells[i];
    diagonalCell.style.backgroundColor = "red";
}