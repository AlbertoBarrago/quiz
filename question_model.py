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
        print(f"{self.username}: \n")
        print(f"Total answers: {self.total_answers} \n"
              f"Total correct answer: {self.correct_answers} \n")
        if self.correct_answers == self.total_answers:
            print(f"All correct! You're a fucking genius!")
        elif self.correct_answers < 2:
            print(f"Poorer idiot! ♥️")

        exit("Game Over")





