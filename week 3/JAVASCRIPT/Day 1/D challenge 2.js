//method 1
let stars = "";
for (let i = 1; i <= 6; i++) {
    stars += "* "; // Add a star and a space to the current string
    console.log(stars); // Print the growing string
}

//method 2
for (let i = 1; i <= 6; i++) {
    let row = ""; 
    // The inner loop runs 'i' times (1 time for row 1, 2 times for row 2...)
    for (let j = 1; j <= i; j++) {
        row += "* ";
    }
    console.log(row);
}