var dropdown = document.getElementById("dropdown");
var text= document.getElementById("text");
var options= document.getElementsByClassName("options");
var list= document.getElementById("list");

dropdown.onclick = function(){
    list.classList.toggle("hide");

}
for(option of options){
    option.onclick = function(){
    text.innerHTML = this.textContent;
    }
};

var swiper = new Swiper(".mySwiper", {
    slidesPerView: 3,
    spaceBetween: 30,
    slidesPerGroup: 3,
    loop: true,
    loopFillGroupWithBlank: true,
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });