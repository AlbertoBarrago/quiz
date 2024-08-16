# Quiz Game
import data
from question_model import QuestionModel


def start_quiz_game():
    print('Welcome to qui game')
    username = input('What is your name? \n')
    want_play = input('Do you want to play (yes/no)?\n')
    if want_play == 'yes':
        question_model = QuestionModel(username, data.question_data)
        question_model.get_questions()




if __name__ == '__main__':
    start_quiz_game()

