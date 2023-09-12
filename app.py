from flask import Flask, request, render_template, redirect
from surveys import Survey, satisfaction_survey


# create a Flask application object named app
app = Flask(__name__)

# needed for the debugger 
app.config['SECRET_KEY'] = "I love kitties"

# empty list to capture survey answers
responses = []

# survey title and instructions for use throughtout the app
title = satisfaction_survey.title
instructions = satisfaction_survey.instructions

# root page
@app.route('/')
def home_page():
  return render_template('index.html', title=title, instructions=instructions)

@app.route('/questions/<int:q_id>')
def question_page(q_id):
  # empty list for the questions from the survey object 
  questions = []

  # loop through the questions in the survey and add each one to the questions list, making them iterable
  for question in satisfaction_survey.questions:
    questions.append(question.question)

  # this is the number to display in the h5 in the question page, one more than the index of the question
  q_num = q_id + 1

  # question is the item in the questions list at the index of q_id in the url (this question being asked on the page with index corresponding to url(q_id))
  # question_number is the number to display on the page asking the question
  return render_template('question.html', title=title, question=questions[q_id], question_number = q_num)


  
  # for i, question in satisfaction_survey.questions:
  #   print(satisfaction_survey.questions)
  #   if 0 <= q_id < len(satisfaction_survey.questions):
  #     q_n = question.question
      
      # question_number = q_id + 1
      # # question_number = satisfaction_survey.questions[q_id]
      # 
  

# I want to loop through the questions and assign each index to it's corresponding number in the url
# or do I make a dictionary from the list?








# to print all questions in a survey
# for question in satisfaction_survey.questions:
    # ...:     print(question.question)


# To print each question
# for i, question in enumerate(satisfaction_survey.questions):
#     ...:         print(f"Question {i+1}: {question}")