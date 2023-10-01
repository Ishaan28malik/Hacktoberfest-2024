var buttons = document.querySelectorAll(".drum").length;
    document.addEventListener("keydown", function (event) {
        switch (event.key) {
            case "w":
                var audio = new Audio('sounds/tom-1.mp3');
                audio.play();
                break;
            case "a" : 
                var audio = new Audio('sounds/tom-2.mp3');
                audio.play();
                break;
            case "s" :
                var audio = new Audio('sounds/tom-3.mp3');
                audio.play();
                break;
            case "d" :
                var audio = new Audio('sounds/tom-4.mp3');
                audio.play();
                break;
            case "j" :
                var audio = new Audio('sounds/snare.mp3');
                audio.play();
                break;
            case "k" :
                var audio = new Audio('sounds/crash.mp3');
                audio.play();
                break;
            case "l" :
                var audio = new Audio('sounds/kick-bass.mp3');
                audio.play();
                break;
            default:
                break;
        }
    });
for (var i=0; i<buttons; i++) {
    
    
    document.querySelectorAll(".drum")[i].addEventListener("click", function() {
        var innerHTML = this.innerHTML;
        switch (innerHTML) {
            case "w":
                var audio = new Audio('sounds/tom-1.mp3');
                audio.play();
                break;
            case "a" : 
                var audio = new Audio('sounds/tom-2.mp3');
                audio.play();
                break;
            case "s" :
                var audio = new Audio('sounds/tom-3.mp3');
                audio.play();
                break;
            case "d" :
                var audio = new Audio('sounds/tom-4.mp3');
                audio.play();
                break;
            case "j" :
                var audio = new Audio('sounds/snare.mp3');
                audio.play();
                break;
            case "k" :
                var audio = new Audio('sounds/crash.mp3');
                audio.play();
                break;
            case "l" :
                var audio = new Audio('sounds/kick-bass.mp3');
                audio.play();
                break;
            default:
                break;
        }
    });
}
