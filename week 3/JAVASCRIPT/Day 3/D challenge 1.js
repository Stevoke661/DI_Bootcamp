//javascript
// 1. Select the necessary elements
const libForm = document.getElementById('libform');
const libButton = document.getElementById('lib-button');
const shuffleButton = document.getElementById('shuffle-button');
const storySpan = document.getElementById('story');

// 2. Function to generate the story
function generateStory(event) {
    event.preventDefault(); // Prevent page refresh

    // Get input values
    const noun = document.getElementById('noun').value.trim();
    const adjective = document.getElementById('adjective').value.trim();
    const person = document.getElementById('person').value.trim();
    const verb = document.getElementById('verb').value.trim();
    const place = document.getElementById('place').value.trim();

    // 3. Validation: Make sure values are not empty
    if (!noun || !adjective || !person || !verb || !place) {
        alert("Please fill in all the blanks before submitting!");
        return;
    }

    // 4. Create an array of potential stories for the Shuffle bonus
    const stories = [
        `${person} found a ${adjective} ${noun} and decided to ${verb} all the way to ${place}.`,
        `In the middle of ${place}, ${person} realized their ${noun} was too ${adjective} to ${verb}.`,
        `It was a ${adjective} day in ${place} when ${person} grabbed a ${noun} and started to ${verb}!`,
        `While visiting ${place}, ${person} saw a ${adjective} ${noun} and couldn't help but ${verb}.`
    ];

    // Pick a random story from the array
    const randomIndex = Math.floor(Math.random() * stories.length);
    storySpan.textContent = stories[randomIndex];
}

// 5. Bonus: Shuffle logic
function shuffleStory() {
    // We can simply call generateStory, but since it's a separate button, 
    // we use a fake event or just call the logic if fields are filled.
    const fakeEvent = { preventDefault: () => {} };
    generateStory(fakeEvent);
}

// 6. Event Listeners
libForm.addEventListener('submit', generateStory);
shuffleButton.addEventListener('click', shuffleStory);