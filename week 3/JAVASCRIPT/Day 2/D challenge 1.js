//java implementation
// 1. Create an array of objects to store planet data
const planets = [
    { name: "Mercury", color: "gray", moons: 0 },
    { name: "Venus", color: "orange", moons: 0 },
    { name: "Earth", color: "blue", moons: 1 },
    { name: "Mars", color: "red", moons: 2 },
    { name: "Jupiter", color: "brown", moons: 79 },
    { name: "Saturn", color: "gold", moons: 82 },
    { name: "Uranus", color: "lightblue", moons: 27 },
    { name: "Neptune", color: "darkblue", moons: 14 }
];

// 2. Select the section where planets will be appended
const section = document.querySelector(".listPlanets");

// 3. Iterate through the array
planets.forEach((planetData) => {
    // Create the planet div
    const planetDiv = document.createElement("div");
    
    // Add the required class
    planetDiv.classList.add("planet");
    
    // Set the background color dynamically
    planetDiv.style.backgroundColor = planetData.color;
    
    // Add text for clarity
    planetDiv.innerText = planetData.name;

    // --- Bonus: Create Moons ---
    for (let i = 0; i < planetData.moons; i++) {
        const moonDiv = document.createElement("div");
        moonDiv.classList.add("moon");
        
        // Position moons so they don't all stack on top of each other
        // This spreads them out in a simple line for visibility
        moonDiv.style.left = (i * 10) + "px"; 
        
        planetDiv.appendChild(moonDiv);
    }

    // 4. Append to the section
    section.appendChild(planetDiv);
});