from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Portal")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        # Text
        self.scoreboard = Label(text="Score: 0", fg="white", background=THEME_COLOR)
        self.scoreboard.grid(row=0, column=1, rowspan=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, width=290,
                                                     text="Random Question",
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Buttons
        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.true_command)
        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.false_command)
        self.false_btn.grid(row=2, column=0)
        self.true_btn.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        self.scoreboard.config(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"You've reached the end of the quiz\n"
                                                            f"You Scored: {self.quiz.score}/"
                                                            f"{self.quiz.question_number}")
            self.scoreboard.config(text="")
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_command(self):
        self.feedback(self.quiz.check_answer("True"))

    def false_command(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)
