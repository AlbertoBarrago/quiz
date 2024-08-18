# Quiz Game
from get_data import QuestionDataService
from question_model import QuestionModel


def start_quiz_game():
    print('Welcome to quiz game by alBz 🥷🏻')
    username = input('What is your name? \n')
    language = input('What is your language? \n')
    length_game = input('How many questions you wants? \n')
    difficulty = input('What difficulty you want (easy/medium/hard)? \n')
    argument_game = input('What is your argument? \n')

    service = QuestionDataService(argument_game, length_game, language, difficulty)
    question_data = service.generate_question_data()

    if length_game:
        question_model = QuestionModel(username, question_data, length_game)
        question_model.get_questions()


if __name__ == '__main__':
    start_quiz_game()

