from tkinter import *

THEME_COLOR = "#375362"


class WelcomePage:

    def __init__(self):
        self.window = Tk()
        self.window.title("Quiz Portal")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.q_category = 0
        self.q_num = 0
        self.start_quiz = False
        self.category = Label(text="Select Category", fg="white", background=THEME_COLOR, font=("Ariel", 10, "bold"))
        self.category.grid(row=0, column=0, pady=10)

        self.category = Label(text="Select Questions", fg="white", background=THEME_COLOR, font=("Ariel", 10, "bold"))
        self.category.grid(row=3, column=0, pady=10)

        # Buttons Category
        self.maths = Button(text="Maths", activebackground="blue", command=self.maths_cat)
        self.maths.grid(row=1, column=0, sticky=EW, padx=10, pady=10)

        self.computer = Button(text="Computer", activebackground="blue", command=self.computer_cat)
        self.computer.grid(row=1, column=1, sticky=EW, padx=10)

        self.science = Button(text="Science & Nature", activebackground="blue", command=self.science_cat)
        self.science.grid(row=1, column=2, sticky=EW, padx=10)

        self.general = Button(text="General Knowledge", activebackground="blue", command=self.general_cat)
        self.general.grid(row=2, column=0, sticky=EW, padx=10)

        self.games = Button(text="Video Games", activebackground="blue", command=self.games_cat)
        self.games.grid(row=2, column=1, sticky=EW, padx=10)

        self.music = Button(text="Music", activebackground="blue", command=self.music_cat)
        self.music.grid(row=2, column=2, sticky=EW, padx=10, pady=10)

        # Buttons Questions
        self.ten = Button(text="10", activebackground="red", command=self.ten_q)
        self.ten.grid(row=4, column=0, sticky=EW, padx=10, pady=10)

        self.twenty = Button(text="20", activebackground="red", command=self.twenty_q)
        self.twenty.grid(row=4, column=1, sticky=EW, padx=10)

        self.fifty = Button(text="50", activebackground="red", command=self.fifty_q)
        self.fifty.grid(row=4, column=2, sticky=EW, padx=10)

        # Submit Button
        self.submit = Button(text="START QUIZ", background="green",
                             activebackground="green", command=self.window.destroy)
        self.submit.grid(row=5, column=1)

        # Credits
        my_credits = Label(text="Everything Tech", fg="white", background=THEME_COLOR, highlightthickness=2)
        my_credits.grid(row=6, column=2, rowspan=1)

        self.window.mainloop()

    # Category Commands
    def maths_cat(self):
        self.q_category = 19

    def computer_cat(self):
        self.q_category = 18

    def science_cat(self):
        self.q_category = 17

    def general_cat(self):
        self.q_category = 9

    def games_cat(self):
        self.q_category = 15

    def music_cat(self):
        self.q_category = 12

    # Question Commands
    def ten_q(self):
        self.q_num = 10

    def twenty_q(self):
        self.q_num = 20

    def fifty_q(self):
        self.q_num = 50
