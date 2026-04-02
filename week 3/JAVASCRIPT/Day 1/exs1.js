//exs1
//part 1
const people = ["Greg", "Mary", "Devon", "James"];

// 1. Remove "Greg"
people.shift(); 

// 2. Replace "James" with "Jason"
people[people.indexOf("James")] = "Jason";

// 3. Add your name to the end
people.push("Gemini");

// 4. Console.log Mary's index
console.log(people.indexOf("Mary")); // Should be 0 now that Greg is gone

// 5. Slice the array (Excluding "Mary" and "Gemini")
// Current array: ["Mary", "Devon", "Jason", "Gemini"]
const slicedPeople = people.slice(1, 3); 
console.log(slicedPeople); // ["Devon", "Jason"]

// 6. Index of "Foo"
console.log(people.indexOf("Foo")); 
// Why -1? Because "Foo" does not exist in the array. indexOf returns -1 by design for missing elements.

// 7. Create variable 'last'
let last = people[people.length - 1];

//part2
// 1. Iterate and log everyone
for (let person of people) {
    console.log(person);
}

// 2. Iterate and exit after "Devon"
for (let person of people) {
    console.log(person);
    if (person === "Devon") {
        break;
    }
}

//exs2
const colors = ["blue", "green", "purple", "black", "silver"];
const suffixes = ["st", "nd", "rd", "th", "th"];

for (let i = 0; i < colors.length; i++) {
    // Basic version: console.log(`My #${i + 1} choice is ${colors[i]}`);
    
    // Bonus version
    let suffix = suffixes[i];
    console.log(`My ${i + 1}${suffix} choice is ${colors[i]}`);
}

//exs3
let number;

// A 'do...while' loop is perfect here because we want to ask 
// at least once regardless of the starting condition.
do {
    let input = prompt("Please enter a number:");
    number = Number(input); // Convert string to number
} while (number < 10);

//exs4
const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

// 2. Number of floors
console.log(building.numberOfFloors);

// 3. Apartments on floor 1 and 3
console.log(building.numberOfAptByFloor.firstFloor + building.numberOfAptByFloor.thirdFloor);

// 4. Second tenant (Dan) and his rooms
let secondTenant = building.nameOfTenants[1];
let danRooms = building.numberOfRoomsAndRent.dan[0];
console.log(`${secondTenant} has ${danRooms} rooms.`);

// 5. Rent check
let sarahRent = building.numberOfRoomsAndRent.sarah[1];
let davidRent = building.numberOfRoomsAndRent.david[1];
let danRent = building.numberOfRoomsAndRent.dan[1];

if (sarahRent + davidRent > danRent) {
    building.numberOfRoomsAndRent.dan[1] = 1200;
    console.log("Dan's rent updated to 1200");
}

//exs5
const family = {
    father: "Homer",
    mother: "Marge",
    son: "Bart"
};

for (let key in family) {
    console.log(key); // Prints: father, mother, son
}

for (let key in family) {
    console.log(family[key]); // Prints: Homer, Marge, Bart
}

//exs6
const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
}

let sentence = "";
for (let key in details) {
    sentence += `${key} ${details[key]} `;
}
console.log(sentence.trim());

//exs7
const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let initials = [];

for (let name of names) {
    initials.push(name[0]); // Get first letter
}

// Sort alphabetically and join into a string
let secretName = initials.sort().join("");
console.log(secretName); // "ABJKPS"