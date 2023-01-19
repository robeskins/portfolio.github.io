
let squaretitle = document.querySelectorAll('div.squaretitle');
let squarecontent = document.querySelectorAll('div.squarecontent');
let square1 = document.getElementById('1')
let square = document.querySelectorAll('div.square');

for(let i = 0; i < square.length; i++){
    square[i].addEventListener('mouseenter', function handleClick(event) {
        squaretitle[i].setAttribute('style', 'display: none;');
    });
};


for(let i = 0; i < square.length; i++){
    square[i].addEventListener('mouseenter', function handleClick(event) {
        squarecontent[i].setAttribute('style', 'display: inline;');
    });
};

for(let i = 0; i < square.length; i++){
    square[i].addEventListener('mouseleave', function handleClick(event) {
        squaretitle[i].setAttribute('style', 'display: inline;');
    });
};

for(let i = 0; i < square.length; i++){
    square[i].addEventListener('mouseleave', function handleClick(event) {
        squarecontent[i].setAttribute('style', 'display: none;');
    });
};



