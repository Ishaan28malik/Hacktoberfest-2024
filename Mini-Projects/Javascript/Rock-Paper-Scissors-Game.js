var userChoice = prompt("Do you choose rock, paper or scissors?");
var computerChoice = Math.random();
if (computerChoice < 0.34) {
  computerChoice = "rock";
} else if (computerChoice <= 0.67) {
  computerChoice = "paper";
} else {
  computerChoice = "scissors";
}
console.log("Computer: " + computerChoice);
compare(userChoice, computerChoice);
var compare = function (choiceA, choiceB) {
  if (choiceA === choiceB) {
    return "The result is a tie!";
  } else if (choiceA === "rock") {
    if (choiceB === "scissors") {
      return "Rock wins";
    } else {
      return "Paper wins";
    }
  } else if (choiceA === "paper") {
    if (choiceB === "rock") {
      return "Paper wins";
    } else {
      return "Scissors wins";
    }
  } else if (choiceA === "scissors") {
    if (choiceB === "rock") {
      return "Rock wins";
    } else {
      return "Scissors wins";
    }
  }
};
