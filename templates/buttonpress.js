const form = document.getElementById('questionForm');


form.addEventListener('submit', function(event) {
  // Prevent the form from submitting normally
  event.preventDefault();

  // Get the data from the form using the FormData object
  const formData = new FormData(form);

  for (let pair of formData.entries()) {
    console.log(pair[0] + ': ' + pair[1]);
  }
  loadHomePage();
});

function loadHomePage(){
  window.location.href = window.location.href.replace("/form", "");
}