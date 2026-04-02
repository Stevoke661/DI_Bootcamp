//exs1
const randomNumber = Math.floor(Math.random() * 100) + 1;
console.log(`The random number is: ${randomNumber}`);

for (let i = 0; i <= randomNumber; i++) {
    if (i % 2 === 0) {
        console.log(i);
    }
}

//exs2
function capitalize(str) {
    let evenCaps = "";
    let oddCaps = "";

    for (let i = 0; i < str.length; i++) {
        if (i % 2 === 0) {
            evenCaps += str[i].toUpperCase();
            oddCaps += str[i].toLowerCase();
        } else {
            evenCaps += str[i].toLowerCase();
            oddCaps += str[i].toUpperCase();
        }
    }

    return [evenCaps, oddCaps];
}

console.log(capitalize("abcdef")); // ['AbCdEf', 'aBcDeF']

//exs3
function isPalindrome(word) {
    const reversed = word.split('').reverse().join('');
    return word === reversed;
}

console.log(isPalindrome("kayak")); // true
console.log(isPalindrome("hello")); // false

//exs4
function biggestNumberInArray(arrayNumber) {
    let max = 0;

    for (let item of arrayNumber) {
        if (typeof item === 'number' && item > max) {
            max = item;
        }
    }
    return max;
}

console.log(biggestNumberInArray([-1, 0, 3, 100, 99, 2, 99])); // 100
console.log(biggestNumberInArray(['a', 3, 4, 2]));             // 4
console.log(biggestNumberInArray([]));                         // 0

//exs5
function getUniqueElements(arr) {
    return [...new Set(arr)];
}

const list = [1, 2, 3, 3, 3, 3, 4, 5];
console.log(getUniqueElements(list)); // [1, 2, 3, 4, 5]

//exs6
function createCalendar(year, month) {
    // JS months are 0-indexed (Jan is 0, Sep is 8)
    const mon = month - 1; 
    const d = new Date(year, mon);

    let table = '<table border="1"><tr><th>MO</th><th>TU</th><th>WE</th><th>TH</th><th>FR</th><th>SA</th><th>SU</th></tr><tr>';

    // Get the first day of the week (0=Sun, 1=Mon... 6=Sat)
    // We adjust it so Mon=0, Tue=1 ... Sun=6
    let dayOfWeek = d.getDay();
    if (dayOfWeek === 0) dayOfWeek = 7; 
    dayOfWeek--; 

    // Add empty cells for the first week
    for (let i = 0; i < dayOfWeek; i++) {
        table += '<td></td>';
    }

    // Fill the cells with dates
    while (d.getMonth() === mon) {
        table += `<td>${d.getDate()}</td>`;

        // If it's Sunday (index 6), start a new row
        if ((dayOfWeek + d.getDate()) % 7 === 0) {
            table += '</tr><tr>';
        }
        d.setDate(d.getDate() + 1);
    }

    // Add empty cells for the last week if necessary
    let lastDay = new Date(year, month, 0).getDay();
    if (lastDay !== 0) {
        for (let i = lastDay; i < 7; i++) {
            table += '<td></td>';
        }
    }

    table += '</tr></table>';
    document.body.innerHTML = table;
}

// Example: September 2012
createCalendar(2012, 9);