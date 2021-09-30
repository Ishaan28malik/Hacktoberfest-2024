var rock = document.querySelector("#rock");
var paper = document.querySelector("#paper");
var scissors = document.querySelector("#scissors");
var playerScoreBoard = document.querySelector("#p-score");
var compScoreBoard = document.querySelector("#c-score");
var playerBox = document.querySelector("#p-box");
var compBox = document.querySelector("#c-box");
var main = document.querySelector("#main")
const selectionArray = ['rock', 'paper', 'scissors'];

const gameStart = () => {
    var playerChoice = playerHand();
    var compChoice = compHand();
    var result = checkPoints(playerChoice, compChoice);
    var gameEnd = updatePoints(result);
    checkGameEnd(gameEnd)
}

const compHand = () => {
    const choice = Math.floor(Math.random()*3)
    const compSelection = selectionArray[choice];
    renderImages(compSelection, 0);
    return compSelection;
}


const playerHand = () => {
    userSelection = event.target.id
    renderImages(userSelection, 1);
    return userSelection
}

const renderImages = (choice, turn) => {
    html = `<img src="./images/${choice}.png"></img>
            <p>${choice.toUpperCase()}</p>
            `
    if(turn == 1){
        playerBox.innerHTML = html;
    }
    else{
        compBox.innerHTML = html;
    }   
}


const updatePoints = (re) => {
    var gameEnd = 0
    if(re == 1){
        pscore = parseInt(playerScoreBoard.textContent, 10)
        pscore += 1;
        playerScoreBoard.textContent = pscore;
    }
    else if(re == -1){
        cscore = parseInt(compScoreBoard.textContent, 10)
        cscore += 1;
        compScoreBoard.textContent = cscore;
    }
    else{
        console.log("")
    }
    if(pscore == 5){
        gameEnd = 1
    }
    else if(cscore == 5){
        gameEnd = 2
    }
    else{
        console.log("")
    }

    return gameEnd
}


const checkPoints = (pc , cc) => {
    var flag = 0 // won = 1, lost = -1 , tie = 0

    if(pc == 'rock' && cc == 'rock'){
        flag = 0;
        console.log('tie');
    }
    else if(pc == 'rock' && cc == 'paper'){
        flag = -1;
        console.log('lost');
    }
    else if(pc == 'rock' && cc == 'scissors'){
        flag = 1;
        console.log('won');
    }
    else if(pc == 'paper' && cc == 'paper'){
        flag = 0;
        console.log('tie');
    }
    else if(pc == 'paper' && cc == 'rock'){
        flag = 1;
        console.log('won');
    }
    else if(pc == 'paper' && cc == 'scissors'){
        flag = -1;
        console.log('lost');
    }
    else if(pc == 'scissors' && cc == 'scissors'){
        flag = 0;
        console.log('tie');
    }
    else if(pc == 'scissors' && cc == 'rock'){
        flag = -1;
        console.log('lost');
    }
    else if(pc == 'scissors' && cc == 'paper'){
        flag = 1;
        console.log('won');
    }
    else{
        flag = 0;
        console.log("Error!");
    }

    return flag;
}

const checkGameEnd = (ge) => {
    if(ge == 1){
        msg = `
                <p>You win!</p>
                <a href="./home.html"><button >Home</button></a>
            `
        endScreen = document.createElement('div')
        endScreen.innerHTML = msg;
        endScreen.classList.add("end-screen-player-win")
        main.append(endScreen);
    }
    else if(ge == 2){
        msg = `
                <p>Comp win!</p>
                <a href="./home.html"><button >Home</button></a>
            `
        endScreen = document.createElement('div')
        endScreen.innerHTML = msg;
        endScreen.classList.add("end-screen-comp-win")
        main.append(endScreen);
    }
}


rock.addEventListener('click', gameStart)
paper.addEventListener('click', gameStart)
scissors.addEventListener('click', gameStart)