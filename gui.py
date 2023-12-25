from bs4 import BeautifulSoup
from tkinter import *

answering = True

class QuizQuestion:
    def __init__(self, text, choices, right, is_raw):
        if is_raw:
            self.text = text
            self.choices = [item[3:].strip() for item in choices.split('\n') if item[3:].strip()]
            self.right = right.replace('The correct answer is:', '').strip()
        else:    
            self.text = text
            self.choices = choices
            self.right = right

def end_answer():
    global answering
    answering = False

def main():
    html_doc = open('01.html').read()
    soup = BeautifulSoup(html_doc, 'html.parser')

    questions = soup.find_all(class_='qtext')
    answers = soup.find_all(class_='answer')
    right_answers = soup.find_all(class_='rightanswer')
    global quiz
    quiz = []

    for i in range(len(questions)):
        question = questions[i].get_text()
        choices = answers[i].get_text()
        right_answer = right_answers[i].get_text()

        for i in quiz:
            if question == i.text:
                continue

        quiz_q = QuizQuestion(question, choices, right_answer, True)
        quiz.append(quiz_q)
    
    setup_quiz()
    run_quiz(0)

def setup_quiz():
    global window
    window = Tk()


def run_quiz(index):
    for element in window.winfo_children():
        element.destroy()
    if len(quiz) > 0:
        question = quiz[index]
        q_text = Label(text=question.text)
        q_text.pack()
        for choice in question.choices:
            q_choice = Button(text=choice, command=lambda:run_quiz(index+1), )
            q_choice.pack()

        window.mainloop()
            

if __name__ == "__main__":
    main()
