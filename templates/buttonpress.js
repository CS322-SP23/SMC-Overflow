const questionform=document.getElementsByID("questionForm")
const submit = document.getElementById("submitBtn");
const category = document.getElementById("category");
const message = document.getElementById("message");
const title = document.getElementById("title");

const output = document.getElementById("output");

questionform.addEventListener("click", function(event) {
  event.preventDefault();
  const category = category.value;
  const message = message.value;
  const title =title.value

  output.innerHTML = "Name: " + title + "<br>Message: " + message;
});