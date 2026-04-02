//javascript
// 1. Select the input element
const inputField = document.getElementById('letterInput');

// 2. Add an event listener for 'input'
inputField.addEventListener('input', function(event) {
    // Get the current value of the input
    let value = event.target.value;

    // Use a Regular Expression to find non-letter characters
    // [^a-zA-Z] means "anything that is NOT a lowercase or uppercase letter"
    // 'g' stands for global (find all instances, not just the first one)
    const cleanValue = value.replace(/[^a-zA-Z]/g, '');

    // 3. Update the input value with the filtered string
    event.target.value = cleanValue;
});