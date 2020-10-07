var len=document.getElementsByClassName("key").length;
for(var i=0;i<len;i++)
{
    document.getElementsByClassName("key")[i].addEventListener("click",function(){
    var keys=this.id;
    soundmadu(keys);
    
    });
}
document.addEventListener("keypress",function(event){
    soundmadu(event.key);
   animationa(event.key);


});
function soundmadu(keys)
{
    switch(keys){
        case "q":
            var c = new Audio("sounds/C.wav");
            c.play();
            break;
        case "w":
                var cc = new Audio("sounds/Cc.wav");
                cc.play();
                break;
        case "e":
                var d = new Audio("sounds/D.wav");
                d.play();
                break;
         case "r":
                    var dd = new Audio("sounds/Dd.wav");
                    dd.play();
                    break;
        case "t":
                        var a = new Audio("sounds/E.wav");
                        a.play();
                        break;
        case "y":
            let a = new Audio("sounds/F.wav");
            a.play();
            break;
        case "u":
             let a = new Audio("sounds/Ff.wav");
             a.play();
             break;
        case "i":
            let a = new Audio("sounds/G.wav");
            a.play();
            break;
         case "o":
                let a = new Audio("sounds/Gg.wav");
                a.play();
                break;
          case "p":
                    let a = new Audio("sounds/A.wav");
                    a.play();
                    break;
          case "[":
                        let a = new Audio("sounds/Aa.wav");
                        a.play();
                        break;
         case "]":
                            let a = new Audio("sounds/B.wav");
                            a.play();
                            break;
    default:break;                                               
    }
}
    function animationa(keys)
    {
        document.getElementById(keys).classList.add("pressed");
        setTimeout(function(){
            document.getElementById(keys).classList.remove("pressed");
        },1000);

        }
    

