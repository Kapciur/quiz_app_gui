from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("QuizzlerApp")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=300, bg="white", highlightthickness=0)
        self.text = self.canvas.create_text(150, 150, width=290, font=("Arial", 20, "italic"), text=f"Text")
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.score.config(text=f"Score: {self.quiz.score}")
            self.canvas.itemconfig(self.text, text=q_text)
        else:
            self.canvas.itemconfig(self.text, text="Out of questions")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

