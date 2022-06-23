from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    question_obj = Question(ques=question_text,ans=question_answer)
    question_bank.append(question_obj)

quiz = QuizBrain(question_bank)    

while quiz.still_has_questions:
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.user_score}/{quiz.question_number}")    