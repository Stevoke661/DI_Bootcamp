//exs1
// Second Part: Hide total tip initially
document.getElementById("totalTip").style.display = "none";

function calculateTip() {
    // First Part: Fetching values
    const billAmount = document.getElementById("billAmt").value;
    const serviceQuality = document.getElementById("serviceQual").value;
    let numberOfPeople = document.getElementById("peopleAmt").value;

    // Condition 1: Validation
    if (serviceQuality == 0 || billAmount === "") {
        alert("Please enter the bill amount and service quality!");
        return; // Stop the function
    }

    // Condition 2: Defaulting people
    if (numberOfPeople === "" || numberOfPeople < 1) {
        numberOfPeople = 1;
        document.getElementById("each").style.display = "none";
    } else {
        document.getElementById("each").style.display = "block";
    }

    // Calculation
    let total = (billAmount * serviceQuality) / numberOfPeople;
    total = total.toFixed(2);

    // Displaying the result
    document.getElementById("totalTip").style.display = "block";
    document.getElementById("tip").innerHTML = total;
}

// Second Part: Event Listener
document.getElementById("calculate").onclick = function() {
    calculateTip();
};

//exs2
const form = document.getElementById("emailForm");

form.onsubmit = function(event) {
    event.preventDefault(); // Stop form from refreshing the page
    const email = document.getElementById("userEmail").value;
    
    console.log("Regex Validation:", validateWithRegex(email));
    console.log("Manual Validation:", validateWithoutRegex(email));
};

// Approach 1: Without Regex
function validateWithoutRegex(email) {
    const atSymbol = email.indexOf("@");
    const dotSymbol = email.lastIndexOf(".");

    // Check if @ exists, . exists after @, and there are chars after .
    if (atSymbol < 1) return false;
    if (dotSymbol <= atSymbol + 2) return false;
    if (dotSymbol === email.length - 1) return false;

    return true;
}

// Approach 2: With Regex
function validateWithRegex(email) {
    const pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return pattern.test(email);
}

//exs3
const btn = document.getElementById("geoBtn");
const display = document.getElementById("displayCoord");

btn.onclick = function() {
    // Check if the browser supports Geolocation
    if (navigator.geolocation) {
        // getCurrentPosition takes a success callback function
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        display.innerHTML = "Geolocation is not supported by this browser.";
    }
};

function showPosition(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    display.innerHTML = `Latitude: ${lat} <br> Longitude: ${lon}`;
}

function showError(error) {
    switch(error.code) {
        case error.PERMISSION_DENIED:
            display.innerHTML = "User denied the request for Geolocation.";
            break;
        case error.POSITION_UNAVAILABLE:
            display.innerHTML = "Location information is unavailable.";
            break;
        case error.TIMEOUT:
            display.innerHTML = "The request to get user location timed out.";
            break;
    }
}