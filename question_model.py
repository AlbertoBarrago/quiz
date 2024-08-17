import time


def check_answer(user_answer, correct_answer, long_answer, current_score):
    """Check if the answer is correct and print the result"""
    if str(user_answer).lower() == str(correct_answer).lower():
        print(f'\nThis is the correct answer'
              f'\nCurrent score: {current_score}')
    else:
        print(f'\nThis is the wrong answer')
        print(f'The correct answer is {correct_answer}')
        print(f'\nCuriosity {long_answer}\n\n')


class QuestionModel:
    """Question Model
     Args:
            username: str
            data: list
        Returns:
            None
    """

    def __init__(self, username, data):
        self.username = username
        self.correct_answers = 0
        self.current_answer = 1
        self.data = data
        self.total_answers = 0

    def get_questions(self):
        for question_list in self.data:
            for element in question_list:
                result = input(f"\nQ{self.current_answer}: {element.get('text')} ?:")
                print("\n\n\n\n")
                if result.lower() == str(element['answer']).lower():
                    self.correct_answers += 1
                self.current_answer += 1
                self.total_answers += 1
                check_answer(result, element.get('answer'), element.get('long_answer'), self.correct_answers)

        self.get_score()

    def get_score(self):
        print(f"\nNice game {self.username} 🚀 \n"
              f"Total answers: {self.total_answers} \n"
              f"Total correct answer: {self.correct_answers} \n")
        if self.correct_answers == len(self.data):
            print(f"All correct! You're a fucking genius!")
        elif self.correct_answers < 2:
            print(f"Poorer idiot! ♥️")
        time.sleep(1)
        exit("Game Over")
