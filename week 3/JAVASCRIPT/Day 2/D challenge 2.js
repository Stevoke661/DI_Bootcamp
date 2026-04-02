//word in a star flame
// 1. Prompt the user for words and split them into an array
const input = prompt("Enter several words separated by commas:");
// We use .map(word => word.trim()) to remove accidental spaces around the commas
const words = input.split(',').map(word => word.trim());

// 2. Find the length of the longest word
let maxLength = 0;
for (const word of words) {
    if (word.length > maxLength) {
        maxLength = word.length;
    }
}

// 3. Define the frame's horizontal border (top and bottom)
// We add 4 to the length: 2 for the stars and 2 for the spaces inside the frame
const border = "*".repeat(maxLength + 4);

// 4. Build and log the frame
console.log(border); // Top Border

for (const word of words) {
    // Calculate how many spaces are needed to reach the maxLength
    const padding = " ".repeat(maxLength - word.length);
    // Construct the line: Star + Space + Word + Padding + Space + Star
    console.log(`* ${word}${padding} *`);
}

console.log(border); // Bottom Border