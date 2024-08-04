// Get the modal
const modal = document.getElementById("myModal");
const modal_content = document.querySelectorAll(".modal-content-gym");

// Get the button that opens the modal
const btn = document.querySelectorAll(".btn-save");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal and the right form
btn.forEach(function(element) {
  element.addEventListener("click", function() {
    modal.style.display = "block";
    if (element.id === "About-boxes") {
      modal_content[0].style.display = "block";
    } else if (element.id === "Images-boxes") {
      modal_content[1].style.display = "block";
    } else if (element.id === "Socialmedia-boxes") {
      modal_content[2].style.display = "block";
    }
  });
});

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
  for (let i = 0; i < modal_content.length; i++) {
    modal_content[i].style.display = "none";
  }
};

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
    for (let i = 0; i < modal_content.length; i++) {
      modal_content[i].style.display = "none";
    }}
  
};