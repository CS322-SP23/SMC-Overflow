// Get the input value and add it to the database
const input = document.getElementById('message-input').value;
addToDatabase(input);

// Get the messages from the database
const messages = getTutorSubjects();

// Display the messages on the screen
const messageList = document.getElementById('message-list');
messages.forEach(message => {
  const messageItem = document.createElement('li');
  messageItem.innerText = message;
  messageList.appendChild(messageItem);
});
