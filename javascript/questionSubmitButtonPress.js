
const form = document.getElementById('questionForm');

form.addEventListener('submit', async (event) => {
  // Prevent the form from submitting normally
  event.preventDefault();

  // Get the data from the form using the FormData object
  const formData = new FormData(form);

  const response = await fetch(window.location.href.replace("/form", "/new-post"), {
    method: 'POST',
    headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    body: new URLSearchParams(formData)
  })

  const data = await response.json();
  loadHomePage();
});

function loadHomePage(){
  window.location.href = window.location.href.replace("/form", "/posts");
}