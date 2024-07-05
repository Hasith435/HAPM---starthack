const quizData = [
    {
        question: "What is the capital of France?",
        answers: [
            { text: "Paris", correct: true },
            { text: "Berlin", correct: false },
            { text: "Madrid", correct: false },
            { text: "Rome", correct: false }
        ]
    },
    {
        question: "Which planet is known as the Red Planet?",
        answers: [
            { text: "Earth", correct: false },
            { text: "Mars", correct: true },
            { text: "Jupiter", correct: false },
            { text: "Saturn", correct: false }
        ]
    },
    {
        question: "Who wrote 'Romeo and Juliet'?",
        answers: [
            { text: "Charles Dickens", correct: false },
            { text: "William Shakespeare", correct: true },
            { text: "Jane Austen", correct: false },
            { text: "Mark Twain", correct: false }
        ]
    }
];

const quizContainer = document.getElementById("quiz");
const resultsContainer = document.getElementById("results");
const submitButton = document.getElementById("submit-btn");

let currentQuestionIndex = 0;
let score = 0;

function startQuiz() {
    showQuestion();
    submitButton.addEventListener("click", checkAnswer);
}

function showQuestion() {
    const currentQuestion = quizData[currentQuestionIndex];
    quizContainer.querySelector(".question").textContent = currentQuestion.question;
    
    const choicesContainer = quizContainer.querySelector(".choices");
    choicesContainer.innerHTML = "";

    currentQuestion.answers.forEach((answer, index) => {
        const button = document.createElement("button");
        button.textContent = answer.text;
        button.classList.add("btn");
        button.addEventListener("click", () => selectAnswer(answer.correct));
        choicesContainer.appendChild(button);
    });
}

function selectAnswer(isCorrect) {
    if (isCorrect) {
        score++;
    }
    currentQuestionIndex++;
    if (currentQuestionIndex < quizData.length) {
        showQuestion();
    } else {
        showResults();
    }
}

function showResults() {
    quizContainer.style.display = "none";
    resultsContainer.innerHTML = `You scored ${score} out of ${quizData.length} questions.`;
    resultsContainer.style.display = "block";
}

function checkAnswer() {
    const selectedOption = quizContainer.querySelector("input[type=radio]:checked");
    if (!selectedOption) {
        alert("Please select an option.");
        return;
    }
    const isCorrect = selectedOption.value === "true";
    selectAnswer(isCorrect);
}

startQuiz();


