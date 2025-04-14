#Luke Duran 04/13/25

class Question:
    def __init__(self, question_text, options, correct_option):
        self.question_text = question_text
        self.options = options  # A list: [option_a, option_b, option_c, option_d]
        self.correct_option = correct_option.upper()  # 'A', 'B', 'C', or 'D'

    def check_answer(self, user_answer):
        return user_answer.upper() == self.correct_option

    def __str__(self):
        return f"{self.question_text}\nA: {self.options[0]}\nB: {self.options[1]}\nC: {self.options[2]}\nD: {self.options[3]}"
