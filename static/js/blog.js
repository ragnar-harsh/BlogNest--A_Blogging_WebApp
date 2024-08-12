// let currentSlideIndex = 0;

// function changeSlide(direction) {
//     const slides = document.querySelectorAll('.slide');
//     currentSlideIndex = (currentSlideIndex + direction + slides.length) % slides.length;
//     updateSlide();
// }

// function currentSlide(index) {
//     currentSlideIndex = index;
//     updateSlide();
// }

// function updateSlide() {
//     const slides = document.querySelector('.slider');
//     const dots = document.querySelectorAll('.dot');
//     slides.style.transform = `translateX(-${currentSlideIndex * 100}%)`;

//     dots.forEach((dot, index) => {
//         dot.classList.toggle('active', index === currentSlideIndex);
//     });
// }

// // Initialize the first dot as active
// document.addEventListener('DOMContentLoaded', () => {
//     document.querySelectorAll('.dot')[0].classList.add('active');
// });




let currentSlideIndex = 0;
let slideInterval;

function changeSlide(direction) {
    const slides = document.querySelectorAll('.slide');
    currentSlideIndex = (currentSlideIndex + direction + slides.length) % slides.length;
    updateSlide();
}

function currentSlide(index) {
    currentSlideIndex = index;
    updateSlide();
}

function updateSlide() {
    const slides = document.querySelector('.slider');
    const dots = document.querySelectorAll('.dot');
    slides.style.transform = `translateX(-${currentSlideIndex * 100}%)`;

    dots.forEach((dot, index) => {
        dot.classList.toggle('active', index === currentSlideIndex);
    });
}

function startAutoSlide() {
    slideInterval = setInterval(() => {
        changeSlide(1);
    }, 3000); // Change slide every 3 seconds
}

function stopAutoSlide() {
    clearInterval(slideInterval);
}

// Initialize the first dot as active and start auto-slide
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('.dot')[0].classList.add('active');
    startAutoSlide();
});

// Add event listeners to stop auto-slide on user interaction
document.querySelector('.prev').addEventListener('click', () => {
    stopAutoSlide();
    changeSlide(-1);
    startAutoSlide(); // Restart auto-slide
});

document.querySelector('.next').addEventListener('click', () => {
    stopAutoSlide();
    changeSlide(1);
    startAutoSlide(); // Restart auto-slide
});

document.querySelectorAll('.dot').forEach((dot, index) => {
    dot.addEventListener('click', () => {
        stopAutoSlide();
        currentSlide(index);
        startAutoSlide(); // Restart auto-slide
    });
});

