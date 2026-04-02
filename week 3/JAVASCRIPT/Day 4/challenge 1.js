//challenge
let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        paid : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}

// 1. Arrow function to display fruits
const displayGroceries = () => {
    groceries.fruits.forEach(fruit => console.log(fruit));
};

// 2. Arrow function to clone and modify
const cloneGroceries = () => {
    // Part 1: Primitive (Pass by Value)
    let user = client; 
    client = "Betty";
    // Question: Will we see "Betty" in the user variable?
    // Answer: No. "user" remains "John" because strings are primitives.
    
    // Part 2: Objects (Pass by Reference)
    let shopping = groceries;
    
    // Modification 1
    groceries.totalPrice = "35$";
    // Question: Will we see this in shopping?
    // Answer: Yes.
    
    // Modification 2
    groceries.other.paid = false;
    // Question: Will we see this in shopping?
    // Answer: Yes.
    
    console.log("User variable:", user);
    console.log("Shopping object totalPrice:", shopping.totalPrice);
    console.log("Shopping object paid status:", shopping.other.paid);
};

// Invoke the function
cloneGroceries();