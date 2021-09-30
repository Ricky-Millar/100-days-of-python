import time
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')

class QuizInterface:

    def __init__(self, quizz_brain : QuizBrain):
        self.quiz = quizz_brain
        self.window = Tk()
        self.window.title('JizzQuiz')
        self.window.config(padx=20, pady =20, bg = THEME_COLOR)
        self.canvas = Canvas(width = 300, height = 250)
        self.tick_button_image = PhotoImage(file="images/true.png")
        self.cross_button_image = PhotoImage(file="images/false.png")
        self.score_counter = Label(text = f'Score: {self.quiz.score}', font = FONT,fg = 'white')
        self.true_button = Button(image=self.tick_button_image, command = lambda :self.answer('True'))
        self.false_button = Button(image=self.cross_button_image, command = lambda : self.answer('False'))
        self.question_text = self.canvas.create_text(150,125,
                                                     width = 290,
                                                     text = 'BANANAGRAM',
                                                     font = FONT)
        self.canvas.grid(column = 0, row = 1, columnspan=2, pady = 50)
        self.score_counter.config(bg=THEME_COLOR)
        self.score_counter.grid(column=1 , row=0 )
        self.true_button.grid(column= 0, row=2 )
        self.false_button.grid(column= 1, row=2 )
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.true_button.config(state = 'disabled')
            self.false_button.config(state='disabled')
            self.canvas.itemconfig(self.question_text, text = f"Finished!\n Score:\n {self.quiz.score}/{self.quiz.question_number}")

    def answer(self, answer):
        if self.quiz.check_answer(answer):
            self.canvas.config(bg = 'green')
            self.canvas.update()
            self.window.after(1000, self.get_next_question)

        else:
            self.canvas.config(bg = 'red')
            self.canvas.update()
            self.window.after(1000, self.get_next_question)

        self.score_counter.config(text = f'Score: {self.quiz.score}')







