const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

// setting time out for error message
setTimeout(function() {
    $('#message').fadeOut('slow')
}, 3000);
