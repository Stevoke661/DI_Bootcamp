//arrays to string conversion
const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];

// Using .toString()
console.log("toString:", numbers.toString()); 
// Output: "5,0,9,1,7,4,2,6,3,8"

// Using .join() with different separators
console.log("join with '+':", numbers.join("+")); // "5+0+9+1+7+4+2+6+3+8"
console.log("join with ' ':", numbers.join(" ")); // "5 0 9 1 7 4 2 6 3 8"
console.log("join with '':", numbers.join(""));   // "5091742638"

//(bonus) code
const number = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];

// Outer loop: Starts from the beginning of the array
for (let i = 0; i < numbers.length; i++) {
    
    // Inner loop: Compares adjacent elements
    // We subtract 'i' because the last 'i' elements are already sorted
    for (let j = 0; j < numbers.length - 1 - i; j++) {
        
        console.log(`Comparing ${numbers[j]} and ${numbers[j+1]}`);

        // For DESCENDING order: swap if the current number is SMALLER than the next
        if (numbers[j] < numbers[j + 1]) {
            
            // 1. Store the current value in a temporary variable
            let temp = numbers[j];
            
            // 2. Move the larger value to the current position
            numbers[j] = numbers[j + 1];
            
            // 3. Put the temporary (smaller) value in the next position
            numbers[j + 1] = temp;
            
            console.log("Swap occurred:", numbers);
        }
    }
    console.log(`--- Pass ${i + 1} complete. Current array: ${numbers} ---`);
}

console.log("Final Sorted Array:", numbers);