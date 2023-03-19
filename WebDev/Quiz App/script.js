const quizData=[
    {
        question: 'Who is the Prime Minister of India ?',
        a: 'Mahatma Gandhi' ,
        b: 'Barac Obama' ,
        c: 'Narender Modi' ,
        d: 'Rahul Gandhi' ,
        correct: 'c'
    },{
        question: 'Who won the FIFA world cup 2002 ?',
        a: 'France' ,
        b: 'Germany' ,
        c: 'Brazil' ,
        d: 'Argentina' ,
        correct: 'c'
    },{
        question: 'Who is the Best Captain of All Time  of Indian Cricket ?',
        a: 'MS Dhoni' ,
        b: 'Virat Kohli' ,
        c: 'Ricky Ponting' ,
        d: 'Saurav Ganguly' ,
        correct: 'a'
    },{
        question: 'Which city is the Tech-Hub of India ?',
        a: 'Mumbai' ,
        b: 'Bangalore' ,
        c: 'Delhi' ,
        d: 'Kolkata' ,
        correct: 'b'
    },{
        question: 'Most Easy Programing Language',
        a: 'C' ,
        b: 'C++' ,
        c: 'Java' ,
        d: 'Python' ,
        correct: 'd'
    }
];
const quiz =document.getElementById("quiz");
const answerEls =document.querySelectorAll(".answer");
const questionEl =document.getElementById('question')
const a_text=document.getElementById('a_text');
const b_text=document.getElementById('b_text');
const c_text=document.getElementById('c_text');
const d_text=document.getElementById('d_text');
const submitBtn =document.getElementById("submit");

let currentQuiz = 0;
let answer =undefined;
let score=0;

loadQuiz();

function loadQuiz(){
    deselectAnswer();
    const currentQuizData = quizData[currentQuiz];
    questionEl.innerText = currentQuizData.question;
    a_text.innerText = currentQuizData.a;
    b_text.innerText = currentQuizData.b;
    c_text.innerText = currentQuizData.c;
    d_text.innerText = currentQuizData.d;

    
}

function getSelected(){  
    let answer =undefined;
    answerEls.forEach((answerEl)=>{
       if(answerEl.checked){
        answer = answerEl.id;
       }
    });

    return answer;
}

function deselectAnswer() {
    answerEls.forEach((answerEl)=>{
       answerEl.checked = false;
        
     });
}

submitBtn.addEventListener('click',()=>{

    const answer = getSelected();

    
    if(answer){
        if(answer === quizData[currentQuiz].correct){
            score++;
        }
        currentQuiz++;        
        if(currentQuiz < quizData.length){
            loadQuiz();
        }
        else{
          quiz.innerHTML=`<h2>Your Score is ${score}/${quizData.length}</h2> <button onclick="location.reload()">Reload</button>`;
        }  
    }
})