import time
from typing import final


class QuestionModel:
    """Question Model """
    def __init__(self, username, data):
        self.username = username
        self.correct_answers = 0
        self.current_answer = 1
        self.data = data

    def get_questions(self):
        for element in self.data:
            result = input(f"Q{self.current_answer}: {element.get('text')} (True/False): ")
            if result == element.get('answer'):
                self.correct_answers += 1
            self.current_answer += 1

        self.get_score()


    def get_score(self):
        print(f"Your score: {self.username}: \n"
              f"Total answers: {self.current_answer} \n"
              f"Total correct answer: {self.correct_answers} \n")
        if self.correct_answers == len(self.data):
            print(f"All correct! You're a fucking genius!")
        elif self.correct_answers < 2:
            print(f"Poorer idiot! ♥️")
        time.sleep(1)
        exit("Game Over")





