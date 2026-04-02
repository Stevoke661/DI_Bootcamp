//exs1
// 1. Create the objects with a method to calculate BMI
const person1 = {
    fullName: "John Doe",
    mass: 80, // in kg
    height: 1.8, // in meters
    calculateBMI: function() {
        this.bmiValue = this.mass / (this.height * this.height);
        return this.bmiValue;
    }
};

const person2 = {
    fullName: "Jane Smith",
    mass: 65,
    height: 1.65,
    calculateBMI: function() {
        this.bmiValue = this.mass / (this.height * this.height);
        return this.bmiValue;
    }
};

// 2. Function to compare BMI
function compareBMI(p1, p2) {
    // Execute the methods to ensure BMI is calculated
    const bmi1 = p1.calculateBMI();
    const bmi2 = p2.calculateBMI();

    if (bmi1 > bmi2) {
        console.log(`${p1.fullName} has the largest BMI (${bmi1.toFixed(2)})`);
    } else if (bmi2 > bmi1) {
        console.log(`${p2.fullName} has the largest BMI (${bmi2.toFixed(2)})`);
    } else {
        console.log("Both have the same BMI.");
    }
}

// Run the comparison
compareBMI(person1, person2);

//exs2
// Part 1 & 2: Calculation Function
function calculateAverage(gradesList) {
    let sum = 0;
    for (let grade of gradesList) {
        sum += grade;
    }
    return sum / gradesList.length;
}

// Part 3 & 4: Logic Function (Calling the first one)
function findAvg(gradesList) {
    // Guard clause: check if array is empty to avoid division by zero
    if (gradesList.length === 0) return console.log("No grades provided.");

    const average = calculateAverage(gradesList);
    console.log(`Average Grade: ${average.toFixed(2)}`);

    if (average > 65) {
        console.log("Congratulations, you passed!");
    } else {
        console.log("You failed and must repeat the course.");
    }
}

// Example usage:
const myGrades = [70, 85, 60, 90, 45];
findAvg(myGrades);