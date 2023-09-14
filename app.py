from flask import Flask, request, render_template, redirect, flash, session
# from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey



# create a Flask application object named app
app = Flask(__name__)


# needed for the debugger 
# app.config['SECRET_KEY'] = "I love kitties"
# debug = DebugToolbarExtension(app)
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False



# empty list to capture survey answers
responses = []

# root page
@app.route('/')
def home_page():
  return render_template('index.html', survey=survey)

@app.route("/answer", methods=["POST"])
def handle_question():
    """Save response and redirect to next question."""

    # get the response choice
    get_choice = request.form['answer']

    # add this response to the session
    responses.append(get_choice)
    print(responses)

    if (len(responses) == len(survey.questions)):
        # They've answered all the questions! Thank them.
        return redirect("/thank-you")

    else:
        return redirect(f"/questions/{len(responses)}")

@app.route('/questions/<int:q_id>')
def question_page(q_id):
  # empty list for the questions from the survey object 
  questions = []

  # loop through the questions in the survey and add each one to the questions list, making them iterable
  for question in survey.questions:
    questions.append(question.question)

  # get the number of questions to redirect after all questions are asked
  num_questions = len(questions)
  print(num_questions)

  # this is the number to display in the h5 in the question page, one more than the index of the question
  q_num = q_id + 1
  
  # the question in the item in the questions list at the index of the q_id in the url
  question = survey.questions[q_id]

  if (responses is None):
     return redirect('/')
  
  if (len(responses) != q_id):
     flash(f'Please answer the questions in order')
     return redirect(f'/questions/{len(responses)}')
     
  # if the question number is less than or equal to the amount of questions, render the question template
  if (q_num <= num_questions):
    # question is the item in the questions list at the index of q_id in the url (the question being asked on the page with index corresponding to url(q_id))
    # question_number is the number to display on the page asking the question
    return render_template('question.html', question_text=questions[q_id], question_number = q_num, question=question, survey=survey)
  
  # if q_num is not a valid question index or the thank you page conditional, go to error page 
  else:
    return redirect('/404')
  
@app.route('/404')
def error_page():
  return render_template('404.html')

@app.route('/thank-you')
def thank_you_page():
  return render_template('thank-you.html', responses=responses)