# Quiz Game
import data
from get_data import QuestionDataService
from question_model import QuestionModel


def start_quiz_game():
    print('Welcome to quiz game')
    username = input('What is your name? \n')
    length_game = input('How many questions you wants? \n')
    argument_game = input('What is your argument? \n')
    # Usage
    service = QuestionDataService(argument_game, length_game)
    question_data = service.generate_question_data()
    if length_game:
        question_model = QuestionModel(username, question_data)
        question_model.get_questions()




if __name__ == '__main__':
    start_quiz_game()

