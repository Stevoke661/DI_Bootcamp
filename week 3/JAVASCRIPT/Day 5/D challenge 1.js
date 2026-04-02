//exs
const tasks = [];
const form = document.getElementById('task-form');
const listContainer = document.querySelector('.listTasks');

form.addEventListener('submit', addTask);

function addTask(event) {
    event.preventDefault(); // Stop page refresh
    
    const input = document.getElementById('task-input');
    const taskText = input.value;

    if (taskText === "") return; // Don't add empty tasks

    // Bonus I: Create task object
    const taskObj = {
        task_id: tasks.length,
        text: taskText,
        done: false
    };

    tasks.push(taskObj);
    renderTask(taskObj);
    input.value = ""; // Clear input
}

function renderTask(task) {
    // Create the main container div
    const taskDiv = document.createElement('div');
    taskDiv.classList.add('task-item');
    taskDiv.setAttribute('data-task-id', task.task_id);

    // 1. The Delete Button (Font Awesome)
    const deleteBtn = document.createElement('i');
    deleteBtn.classList.add('fa-solid', 'fa-xmark');
    deleteBtn.addEventListener('click', () => deleteTask(task.task_id));

    // 2. The Checkbox
    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.addEventListener('change', () => doneTask(task.task_id));

    // 3. The Label
    const label = document.createElement('label');
    label.textContent = task.text;

    // Append everything to the div
    taskDiv.appendChild(deleteBtn);
    taskDiv.appendChild(checkbox);
    taskDiv.appendChild(label);

    // Add the div to the DOM
    listContainer.appendChild(taskDiv);
}

// Bonus I: Mark as Done
function doneTask(id) {
    const taskIndex = tasks.findIndex(t => t.task_id === id);
    tasks[taskIndex].done = !tasks[taskIndex].done;

    // Toggle the CSS class in the DOM
    const taskElement = document.querySelector(`[data-task-id="${id}"]`);
    taskElement.classList.toggle('is-done');
}

// Bonus II: Delete Task
function deleteTask(id) {
    // Remove from array
    const taskIndex = tasks.findIndex(t => t.task_id === id);
    if (taskIndex > -1) {
        tasks.splice(taskIndex, 1);
    }

    // Remove from DOM
    const taskElement = document.querySelector(`[data-task-id="${id}"]`);
    taskElement.remove();
}