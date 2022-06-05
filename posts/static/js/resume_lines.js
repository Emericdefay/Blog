let value;

function setValueHeight() {
    value = window.screen.height;
    console.log(document.querySelector('.navbar').offsetHeight);
    console.log(document.querySelector('#contact-me').offsetHeight);
    console.log(document.querySelector('.left-column').offsetHeight);
    value -= document.querySelector('.navbar').offsetHeight;
    value -= document.querySelector('.contact-me').offsetHeight;
    value -= document.querySelector('.left-column').offsetHeight;
    value *= 1.7;
    console.log(value);
    return value*2;
}

document.addEventListener("DOMContentLoaded", function(event){
    if (window.screen.width < 1051) {
        setValueHeight()
        document.documentElement.style.setProperty('--height-lines', `${1450}px`);
    }
});
