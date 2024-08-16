class QuestionModel:
    """Question Model """
    def __init__(self, username, data):
        self.username = username
        self.correct_answers = 0
        self.total_answers = 0
        self.data = data

    def get_questions(self):
        for element in self.data:
            result = input(element.get('text') + " (True/False): ")
            if result == element.get('answer'):
                self.correct_answers += 1
            self.total_answers += 1

        self.get_score()


    def get_score(self):
        print(f"{self.username}: ")
        print(f"Total answers: {self.total_answers}"
              f"Total correct answer: {self.correct_answers}")
        if self.correct_answers == self.total_answers:
            print(f"Fucking genius!")
            exit("You win!")
        elif self.correct_answers < 4:
            print(f"Poorer idiot!")
            exit("Game Over")
        else:
            exit("Game Over")





