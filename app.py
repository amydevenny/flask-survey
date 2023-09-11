from flask import Flask, request, render_template
from surveys import satisfaction_survey


# create a Flask application object named app
app = Flask(__name__)

# needed for the debugger 
app.config['SECRET_KEY'] = "I love kitties"

# empty list to capture survey answers
responses = []

# root page
@app.route('/')
def home_page():
  return render_template('index.html')

@app.route('/questions/<int:q_id>')
def question_page(q_id):
  # question = satisfaction_survey.questions[q_id]
  for question in satisfaction_survey.questions:
    if 0 <= q_id < len(satisfaction_survey.questions):
      q_n = question.question
      # question_number = q_id + 1
      question_number = satisfaction_survey.questions[q_id]
      return render_template('question.html', question=q_n, question_number = question_number)
  

# I want to loop through the questions and assign each index to it's corresponding number in the url
# or do I make a dictionary from the list?








# to print all questions in a survey
# for question in satisfaction_survey.questions:
    # ...:     print(question.question)


# To print each question
# for i, question in enumerate(satisfaction_survey.questions):
#     ...:         print(f"Question {i+1}: {question}")