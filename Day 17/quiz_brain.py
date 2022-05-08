class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        return (self.question_number < len(self.question_list))

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} Trule or False? \n")
        self.check_answer(user_answer, current_question.answer, self.question_number)

    def check_answer(self, user_answer, correct_answer, question_number):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score} / {question_number}")
        print("\n")
        