import pandas as pd
from bs4 import BeautifulSoup

BLUE = "\033[0;34m"
BOLD = "\033[1m"
LIGHT_GREEN = "\033[1;32m"
LIGHT_BLUE = "\033[1;34m"
YELLOW = "\033[33m"
END = "\033[0m"

class QuizQuestion:
    def __init__(self, text, choices, right):
        self.text = text
        self.choices = choices
        self.right = right

def load_quiz_data(file_path):
    df = pd.read_csv(file_path)
    quiz = []

    for index, row in df.iterrows():
        question = row['QuestionText']
        choices = [row['AnswerA'], row['AnswerB'], row['AnswerC'], row['AnswerD']]
        right_answer = row['CorrectAnswerText']

        quiz_q = QuizQuestion(question, choices, right_answer)

        exists = False
        for i in quiz:
            if i.text == question:
                exists = True
        
        if not exists:      
            quiz.append(quiz_q)

    return quiz

def main():
    quiz = load_quiz_data('questions.csv')

    while len(quiz) > 0:
        print(YELLOW + f"{len(quiz)} questions to go, Keep going!" + END)
        for question in quiz:
            choices = []
            for i in range(len(question.choices)):
                choices.append(chr(65 + i) + " " + question.choices[i])

            choices = "\n".join(choices)
            print(f'\n{BLUE + BOLD + question.text + END}\n{LIGHT_GREEN + choices}')

            user_choice = input(BOLD + LIGHT_BLUE + 'Choose: ' + END)

            try:
                if question.choices[ord(user_choice[0].upper()) - 65] == question.right:
                    quiz.remove(question)
                    print("Correct!")
                else:
                    print("Incorrect!")
            except:
                pass

if __name__ == "__main__":
    main()
