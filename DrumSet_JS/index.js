function handleclick() {
  // this.style.color = "white";
  // var audio = new Audio("sounds/tom-1.mp3");
  // audio.play();
  var buttonInnerHTML = this.innerHTML;
  console.log(buttonInnerHTML);
  switch (buttonInnerHTML) {
    case "w":
      var audio = new Audio("sounds/tom-1.mp3");
      audio.play();
      break;
    case "a":
      var audio = new Audio("sounds/tom-2.mp3");
      audio.play();
      break;
    case "s":
      var audio = new Audio("sounds/tom-4.mp3");
      audio.play();
      break;
    case "d":
      var audio = new Audio("sounds/tom-4.mp3");
      audio.play();
      break;
    case "j":
      var audio = new Audio("sounds/snare.mp3");
      audio.play();
      break;
    case "k":
      var audio = new Audio("sounds/crash.mp3");
      audio.play();
      break;
    default:
      var audio = new Audio("sounds/kick-bass.mp3");
      audio.play();
      break;
  }
  btn_animation(buttonInnerHTML);
}
for (var i = 0; i < document.querySelectorAll(".drum").length; i++) {
  document.querySelectorAll(".drum")[i].addEventListener("click", handleclick);
}

document.addEventListener("keypress", function (e) {
  playSound(e.key);
  btn_animation(e.key)
});

function playSound(key) {
  switch (key) {
    case "w":
      var audio = new Audio("sounds/tom-1.mp3");
      audio.play();
      break;
    case "a":
      var audio = new Audio("sounds/tom-2.mp3");
      audio.play();
      break;
    case "s":
      var audio = new Audio("sounds/tom-4.mp3");
      audio.play();
      break;
    case "d":
      var audio = new Audio("sounds/tom-4.mp3");
      audio.play();
      break;
    case "j":
      var audio = new Audio("sounds/snare.mp3");
      audio.play();
      break;
    case "k":
      var audio = new Audio("sounds/crash.mp3");
      audio.play();
      break;
    default:
      var audio = new Audio("sounds/kick-bass.mp3");
      audio.play();
      break;
  }
}

function btn_animation(key){
  var activeBtn = document.querySelector("." + key);
  activeBtn.classList.add("pressed");

  setTimeout(function(){
    activeBtn.classList.remove("pressed");
  }, 100);
}
