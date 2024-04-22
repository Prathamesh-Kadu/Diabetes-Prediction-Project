// header relative to fixed when scroll down

const header = document.querySelector('.my-header');

const headerScroll = () => {
    window.addEventListener('scroll', () => {
        console.log(window.scrollY);

        if (window.scrollY > 100) {
            header.style.position = "fixed";
        } else {
            header.style.position = "relative";
        }
    });
};


headerScroll();

