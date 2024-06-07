
// shows popup message when click submit on form

document.addEventListener("DOMContentLoaded", function() {
    var contactForm = document.getElementById("contactform");
    var successAlert = document.getElementById("successAlert");

    contactForm.addEventListener("submit", function(event) {
        event.preventDefault();

        if (contactForm.checkValidity()) {
            successAlert.style.display = "block";
            contactForm.reset();
        }
    });
});