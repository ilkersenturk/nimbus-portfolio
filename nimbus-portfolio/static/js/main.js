// Accordion logic
document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll(".accordion").forEach(button => {
      button.addEventListener("click", function () {
        const panel = this.nextElementSibling;
        panel.classList.toggle("open");
      });
    });
  });
  
  // Form validation
  function validateForm() {
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const message = document.getElementById("message").value.trim();
    if (!name || !email || !message) {
      alert("Please fill out all fields.");
      return false;
    }
    alert("Thanks! Your message has been sent.");
    return true;
  }
  