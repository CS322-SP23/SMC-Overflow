const fs = require("fs");
const form = document.getElementById('questionForm');
let postsjson = fs.readFileSync("../test_data/posts.json","utf-8");
let posts= json.parse(postsjson);

form.addEventListener('submit', function(event) {
  // Prevent the form from submitting normally
  event.preventDefault();

  // Get the data from the form using the FormData object
  const formData = new FormData(form);

  for (let pair of formData.entries()) {
    console.log(pair[0] + ': ' + pair[1]);
  }
  posts.push(formData.entries);
  loadHomePage();
});

function loadHomePage(){
  window.location.href = window.location.href.replace("/form", "/posts");
}