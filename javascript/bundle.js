(function(){function r(e,n,t){function o(i,f){if(!n[i]){if(!e[i]){var c="function"==typeof require&&require;if(!f&&c)return c(i,!0);if(u)return u(i,!0);var a=new Error("Cannot find module '"+i+"'");throw a.code="MODULE_NOT_FOUND",a}var p=n[i]={exports:{}};e[i][0].call(p.exports,function(r){var n=e[i][1][r];return o(n||r)},p,p.exports,r,e,n,t)}return n[i].exports}for(var u="function"==typeof require&&require,i=0;i<t.length;i++)o(t[i]);return o}return r})()({1:[function(require,module,exports){

},{}],2:[function(require,module,exports){
const fs = require('fs');
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
},{"fs":1}]},{},[2]);
