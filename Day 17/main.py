# Day 17 of Angela Yu's "100 Days of Python" on udemy.

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    individual_question = Question(question_text, question_answer)
    question_bank.append(individual_question)

quiz = QuizBrain(question_bank)
quiz.next_question()