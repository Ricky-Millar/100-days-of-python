class QuizzBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        correct_answer = current_question.answer
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}:{current_question.text} True or False?")
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"\nCorrect! current score: {self.score}/{self.question_number}\n")
        else:
            print(f"\nWrong answer. current score: {self.score}/{self.question_number}\n")
