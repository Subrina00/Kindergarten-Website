let loginForm = document.querySelector('.login-form');
let navbar = document.querySelector('.navbar');

document.querySelector('#login-btn').onclick = () =>{
    loginForm.classList.toggle('active');
    navbar.classList.remove('active');
}


document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
    loginForm.classList.remove('active');
}

window.onscroll = () =>{
    loginForm.classList.remove('active');
    navbar.classList.remove('active');
}