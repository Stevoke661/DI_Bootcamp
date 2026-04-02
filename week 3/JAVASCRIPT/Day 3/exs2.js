//exs1
// Part I: Simple Alert
setTimeout(function() {
    alert("Hello World");
}, 2000);

// Part II & III: Adding Paragraphs and Intervals
const container = document.getElementById("container");
const clearBtn = document.getElementById("clear");

// We'll use a variable to store the interval ID so we can stop it later
let intervalId;

function addParagraph() {
    const newP = document.createElement("p");
    newP.textContent = "Hello World";
    container.appendChild(newP);

    // Part III: Stop if there are 5 paragraphs
    const pCount = container.querySelectorAll("p").length;
    if (pCount >= 5) {
        stopInterval();
    }
}

// Start the interval
intervalId = setInterval(addParagraph, 2000);

// Function to clear the interval
function stopInterval() {
    clearInterval(intervalId);
    console.log("Interval Cleared");
}

// Clear interval when button is clicked
clearBtn.addEventListener("click", stopInterval);

//exs2
// java implementation
function myMove() {
  const elem = document.getElementById("animate");
  let pos = 0; // Starting position
  
  // Set the interval to run every 1ms
  const id = setInterval(frame, 1);

  function frame() {
    // Check if the box has reached the right edge (400 - 50 = 350)
    if (pos === 350) {
      clearInterval(id);
    } else {
      pos++; 
      elem.style.left = pos + "px"; // Update the CSS property
    }
  }
}