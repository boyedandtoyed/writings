let login = document.querySelector('.login');
let register = document.querySelector('.register');
let hiddenpopper = document.querySelector('.hiddenpopper');

function changePopper(e){
    hiddenpopper.style.display = 'block';
    hiddenpopper.style.transform = 'scale(1000)';
    hiddenpopper.style.backgroundColor = getComputedStyle(e.target).color;
}


login.addEventListener('click', changePopper)

register.addEventListener('click',changePopper)

