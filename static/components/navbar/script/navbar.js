let toggle = document.querySelector('.toggle')
let toggleButton = document.querySelector('.toggle .button')
let root = document.querySelector(':root')
let hamregion = document.querySelector('.hamregion')
let ulInHead = document.querySelector('nav ul')

let bluepen = document.querySelector('.penblue')
let greenpen = document.querySelector('.pengreen')

const lighttext = document.querySelector('.toggle .lighttext')
const darktext = document.querySelector('.toggle .darktext')
const darkBackground = getComputedStyle(root).getPropertyValue( '--dark-back');
const textDuringDark =  getComputedStyle(root).getPropertyValue('--text-during-dark')
const lightBackground =  getComputedStyle(root).getPropertyValue('--light-back')
const textDuringLight =  getComputedStyle(root).getPropertyValue('--text-during-light')

function toggleFUNC(e) {
    { 
        // if background is dark
        if ( getComputedStyle(root).getPropertyValue('--rootback-color') == darkBackground) {
            // change it to light back
            root.style.setProperty('--rootback-color', lightBackground );
            // dark text i.e textfor light back
            root.style.setProperty('--root-text-color', textDuringLight );
            //disapear lighttext, so that there is no make light button
            lighttext.style.display = 'none';
            // appear darktext, so that there is make dark button
            darktext.style.display = 'block';
            // the button should move to right
            greenpen.style.display = 'inline-block'
            bluepen.style.display = 'none';
            toggleButton.style.left = '100px';

        } else { //justaopposite , if background is light
            root.style.setProperty('--rootback-color', darkBackground);
            root.style.setProperty('--root-text-color', textDuringDark );
            darktext.style.display = 'none';
            lighttext.style.display = 'block';
            greenpen.style.display = 'none';
            bluepen.style.display = 'inline-block';
            toggleButton.style.left = '0px';
        }
    }
}

toggle.addEventListener('click', toggleFUNC);

toggle.addEventListener('keypress', (e) => {
    if ((e.key == 'Enter') || (e.key == ' ')) {
        toggleFUNC();
    }
})

hamregion.addEventListener('click', (e) => {
    hamregion.classList.toggle('cross');
    ulInHead.classList.toggle('small');
})
// hamregion.addEventListener('focus',(e) =>{
//     hamregion.classList.add('cross');
// })

hamregion.addEventListener('keypress', (e) => {
    if ((e.key == 'Enter') || (e.key == ' ')) {
        hamregion.classList.toggle('cross');
        ulInHead.classList.toggle('small');
    }
})
window.addEventListener('resize', (e) => {
    let display = getComputedStyle(hamregion).display;
    if (display == 'none') {
        hamregion.classList.remove('cross');
        ulInHead.classList.remove('small');
    }
})