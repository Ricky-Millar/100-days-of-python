from question_model import Question
from quiz_brain import QuizzBrain
from data import question_data
question_bank = []
for i in question_data:
    text = i['question']
    answer = i['correct_answer']
    question = Question(text, answer)
    question_bank.append(question)

quiz = QuizzBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print('\nYou completed the quiz')
print(f'your final score is: {quiz.score}/{quiz.question_number}')