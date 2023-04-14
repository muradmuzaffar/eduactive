const swiper = new Swiper('.main-swiper', {
  // Optional parameters
  direction: 'horizontal',
  loop: true,
  speed: 200,
  loop: false,
  grabCursor: true,
  preventClicks: true,
  slidesPerView: 4,
  slidesPerGroup: 1,
  spaceBetween: 20,

  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },
  breakpoints: {
    0: {
      slidesPerView: 1.1,
    },
    420: {
      slidesPerView: 1.3,
    },
    480: {
      slidesPerView: 1.5
    },
    540: {
      slidesPerView: 1.7
    },
    576: {
      slidesPerView: 1.5,
    },
    767: {
      slidesPerView: 2.2,
    },
    992: {
      slidesPerView: 3,
    },
    1200: {
      slidesPerView: 3.5,
    },
    1400: {
      slidesPerView: 4,
    }
  }
});

// Login Form Validation
(() => {
  'use strict'

  const forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.from(forms).forEach(form => {
    form.addEventListener('submit', event => {
      if (!form.checkValidity()) {
        event.preventDefault()
        event.stopPropagation()
      }

      form.classList.add('was-validated')
    }, false)
  })
})()

// Show password

const showPassword = (button, input) => {

  $(button).click(function () {
    if ($(input).attr('type') == 'password') {
      $(input).attr('type', 'text');
    } else {
      $(input).attr('type', 'password');
    }
  });
}

showPassword('#showHidePass', '#id_password')
showPassword('#showHidePass2', '#id_password1')