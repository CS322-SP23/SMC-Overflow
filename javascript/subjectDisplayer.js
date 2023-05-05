// Get the form element
const form = document.getElementById('subject-form');

// Add an event listener to the form submit button
form.addEventListener('submit', (event) => {
  event.preventDefault(); // prevent the default form submission

  // Get the input value and add it to the database
  const input = document.getElementsByName('subject')[0].value;
  addToDatabase(input);

  // Get the messages from the database
  const messages = getTutorSubjects();

  // Display the messages on the screen
  const messageList = document.getElementById('TutorSubject');
  messageList.innerHTML = ''; // clear the existing messages
  messages.forEach(message => {
    const messageItem = document.createElement('li');
    messageItem.innerText = message;
    messageList.appendChild(messageItem);
  });
});
