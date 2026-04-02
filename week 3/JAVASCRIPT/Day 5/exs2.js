//exs1
// 1. Function to play the sound
function playSound(e) {
  // Select audio element where data-key matches the pressed key
  const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
  const key = document.querySelector(`.key[data-key="${e.keyCode}"]`);

  if (!audio) return; // Stop the function if no audio matches

  audio.currentTime = 0; // Rewind to start so we can hit it fast
  audio.play();

  key.classList.add('playing'); // Add your CSS "active" style
}

// 2. Function to remove the animation
function removeTransition(e) {
  if (e.propertyName !== 'transform') return; // Skip if it's not a transform
  this.classList.remove('playing');
}

// 3. Event Listeners
const keys = document.querySelectorAll('.key');
keys.forEach(key => key.addEventListener('transitionend', removeTransition));
window.addEventListener('keydown', playSound);