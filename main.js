import quizData from './questions.js'

const questionEl = document.getElementById('question');
const a_text = document.getElementById('a_text');
const b_text = document.getElementById('b_text');
const c_text = document.getElementById('c_text');
const d_text = document.getElementById('d_text');
const submitBtn = document.getElementById('submit');
const restartBtn = document.getElementById('restart');


let currentQuiz = 0;
let userOptions = []
let userScore = 0

console.log(quizData)

function isValidate() {
    if (!document.getElementById('a').checked &&
        !document.getElementById('b').checked &&
        !document.getElementById('c').checked &&
        !document.getElementById('d').checked) {
        alert("Please select an option pleaseeeeeeeeeeeeeeeeeeeeeee!")
        return false  //if you'll not write this return statement then alert will show but move to next question. 
    }
    return true
}

loadQuiz();
function loadQuiz() {
    const currentQuizData = quizData[currentQuiz];
    questionEl.innerText = currentQuizData.question;
    a_text.innerText = currentQuizData.a;
    b_text.innerText = currentQuizData.b;
    c_text.innerText = currentQuizData.c;
    d_text.innerText = currentQuizData.d;
}

submitBtn.addEventListener("click", () => {
    if(isValidate()) {

        if (document.getElementById('a').checked)
            userOptions.push('a')
        else if (document.getElementById('b').checked)
            userOptions.push('b')
        else if (document.getElementById('c').checked)
            userOptions.push('c')
        else if (document.getElementById('d').checked)
            userOptions.push('d')

        document.getElementById('a').checked = false 
        document.getElementById('b').checked = false
        document.getElementById('c').checked = false
        document.getElementById('d').checked = false
        //if we'll not write the above four lines then the selected option of current question will already got selected for next question.

        if (currentQuiz < quizData.length - 1) {  //if you write only length not length - 1 then the last question will repeat twice
            currentQuiz++;
            loadQuiz();
        } else {
            // alert('all finished')
            for (var i = 0; i < quizData.length; i++) {
                if (userOptions[i] == quizData[i].correct) {
                    userScore++
                }
                console.log(userOptions[i] + ' - ' + quizData[i].correct)
            }
            console.log('score is ' + userScore)
            document.getElementById('score-text').innerText = userScore
            document.getElementById('quiz').style.display = 'none'
            document.getElementById('result').style.display = 'block'

        }
    }
});
restartBtn.addEventListener("click", () => {

    window.location.reload()
});
