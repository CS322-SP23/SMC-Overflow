
const form = document.getElementById('questionForm');
let postsjson = readFileSync("../test_data/posts.json","utf-8");
let posts= json.parse(postsjson);

form.addEventListener('submit', function(event) {
  // Prevent the form from submitting normally
  event.preventDefault();

  // Get the data from the form using the FormData object
  const formData = new FormData(form);

  const formDataJson = JSON.stringify(Object.fromEntries(formData.entries()));
  posts.push(formDataJson);
  loadHomePage();
});

function loadHomePage(){
  window.location.href = window.location.href.replace("/form", "/posts");
}