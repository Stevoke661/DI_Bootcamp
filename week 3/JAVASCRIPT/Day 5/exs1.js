//exs1
let isDrawing = false;
let selectedColor = 'black'; // Default color

//exs2
const container = document.getElementById('grid-container');

for (let i = 0; i < 2500; i++) {
    const square = document.createElement('div');
    square.classList.add('square');
    
    // Add the drawing logic here
    square.addEventListener('mousedown', () => {
        isDrawing = true;
        square.style.backgroundColor = selectedColor;
    });

    square.addEventListener('mouseover', () => {
        if (isDrawing) {
            square.style.backgroundColor = selectedColor;
        }
    });

    container.appendChild(square);
}

// Stop drawing when mouse is released anywhere on the window
window.addEventListener('mouseup', () => {
    isDrawing = false;
});