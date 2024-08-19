import textwrap
import time


def check_answer(user_answer, correct_answer, long_answer, current_score, total_answers):
    """Check if the answer is correct and print the result"""
    if str(user_answer).lower() == str(correct_answer).lower():
        print(f'\nThis is the correct answer'
              f'\nCurrent score: {current_score}/{total_answers}')
    else:
        print(f'\nThis is the wrong answer')
        print(f'The correct answer is {correct_answer}')
        wrapped_answer = textwrap.fill(long_answer, width=80)
        print(f'\nCuriosity:\n{wrapped_answer}\n\n')


class QuestionModel:
    """Question Model
     Args:
            username: str
            data: list
        Returns:
            None
    """

    def __init__(self, username, data, game_length):
        self.username = username
        self.correct_answers = 0
        self.current_answer = 1
        self.data = data
        self.total_answers = int(game_length)

    def get_questions(self):
        for question_list in self.data:
            for element in question_list:
                text_wrap = textwrap.fill(element.get('text'), width=80)
                result = input(f"\nQ{self.current_answer} - {text_wrap}? ").strip()
                if result.lower() == str(element['answer']).lower():
                    self.correct_answers += 1
                self.current_answer += 1
                check_answer(result, element.get('answer'), element.get('long_answer'), self.correct_answers, self.total_answers)

        self.get_score()

    def get_score(self):
        print(f"\nNice game {self.username} 🚀 \n"
              f"Total answers: {self.total_answers} \n"
              f"Total correct answer: {self.correct_answers} \n")
        if self.correct_answers == self.total_answers:
            print(f"All correct! You're a genius! ")
        elif self.correct_answers == 0:
            print(f"Lol have you acquire the 47th! chromosome (Klinefelter powa) ♥️")
        time.sleep(1)
        exit("Game Over ")
