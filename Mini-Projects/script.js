const quizData = 
[
    
    {
        question: '1 Terabyte (Tb) =',
        a:'1,024 Gb',
        b:'1,000 Gb',
        c:'1,200 Gb',
        d:'1220 Gb',
        correct:'a'
    },
    {
        question: 'Which is the best Programming language?',
        a:'Java',
        b:'Python',
        c:'C',
        d:'Javascript',
        correct:'c'
    },
    {
        question: 'If you restart your computer by selecting the restart button, it is known as …',
        a:'Softboot',
        b:'Cold boot',
        c:'Warm boot',
        d:'A and C',
        correct:'d'
    }, {
        question: 'What does HTML stant for?',
        a:'Hypertext Markup Language',
        b:'Cascading stylesheet',
        c:'Jason Object Notation',
        d:'Object Oriented Programming',
        correct:'a'
    },{
        question: 'When was the javascript launched?',
        a:'2020',
        b:'2019',
        c:'2018',
        d:'none of the above',
        correct: 'd'
    },{
        question: ' Which among the following is the shortcut key for Help in your computer system?',
        a:'F1',
        b:'F2',
        c:'f3',
        d:'Ctrl + F',
        correct: 'a'
    },{
        question: 'Byte is the series of ……………… bits.',
        a:'2',
        b:'5',
        c:'8',
        d:'12',
        correct: 'c'
    },{
        question: 'n a network system, which among the following is the most powerful computer?',
        a:'Laptop',
        b:'Desktop',
        c:'Server',
        d:'Notebook',
        correct: 'c'
    }


];

const quiz = document.getElementById("quiz");
const answerEls = document.querySelectorAll(".answer");
const questionEl = document.getElementById("question");
const a_text = document.getElementById("a_text");
const b_text = document.getElementById("b_text");
const c_text = document.getElementById("c_text");
const d_text = document.getElementById("d_text");
const submitBtn = document.getElementById("submit");

let currentQuiz = 0;
let score = 0;

loadQuiz();

function loadQuiz() {
    deselectAnswers();

    const currentQuizData = quizData[currentQuiz];

    questionEl.innerText = currentQuizData.question;
    a_text.innerText = currentQuizData.a;
    b_text.innerText = currentQuizData.b;
    c_text.innerText = currentQuizData.c;
    d_text.innerText = currentQuizData.d;
}

function getSelected() {
    let answer = undefined;

    answerEls.forEach((answerEl) => {
        if (answerEl.checked) {
            answer = answerEl.id;
        }
    });

    return answer;
}

function deselectAnswers() {
    answerEls.forEach((answerEl) => {
        answerEl.checked = false;
    });
}

submitBtn.addEventListener("click", () => {
    // check to see the answer
    const answer = getSelected();

    if (answer) {
        if (answer === quizData[currentQuiz].correct) {
            score++;
        }

        currentQuiz++;
        if (currentQuiz < quizData.length) {
            loadQuiz();
        } else {
            quiz.innerHTML = `
                <h2>You answered correctly at ${score}/${quizData.length} questions.</h2>
                
                <button onclick="location.reload()">Reload</button>
            `;
        }
    }
});