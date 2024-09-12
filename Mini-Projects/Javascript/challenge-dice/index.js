function rollTheDices(){
  var dice1 = Math.floor(Math.random() * 6) + 1,
      dice2 = Math.floor(Math.random() * 6) + 1,
      header = document.querySelector(".game h1");

      drawDices(1,dice1);
      drawDices(2,dice2);

      if(dice1  === dice2){
        header.innerHTML = "Draw! " + "👊🏻😎";
      } else if ( dice1 > dice2 ) {
        header.innerHTML = "Player 1 Wins! " + "🚩";
      } else {
        header.innerHTML = "Player 2 Wins! " + "🚩";
      }
}


function drawDices(player, dice){
  var positions = [],
      dots = [];

    if(dice === 6) {
        positions = [["left","","right"],["left","","right"],["left","","right"]];
    } else if(dice === 5) {
        positions = [["left","","right"],["","center",""],["left","","right"]];
    } else if(dice === 4) {
        positions = [["left","","right"],["","",""],["left","","right"]];
    } else if(dice === 3) {
        positions = [["left","",""],["","center",""],["","","right"]];
    } else if(dice === 2) {
        positions = [["left","",""],["","",""],["","","right"]];
    } else {
        positions = [["","",""],["","center",""],["","",""]];
    }

   for(var collums = 0; collums < positions.length; collums++){

       dots = document.querySelector("#player" + player + " .collum" + (collums + 1) ).querySelectorAll("span");

       for(var rows = 0; rows < positions[collums].length; rows++ ) {

           dots[rows].classList = [];

           if (positions[collums][rows] != ""){
               dots[rows].classList.add("dot");
               dots[rows].classList.add(positions[collums][rows]);
           }
       }
   }

}
