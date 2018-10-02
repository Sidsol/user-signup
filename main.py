from flask import Flask, request, redirect, render_template
import cgi
import os


app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():

    return render_template('user_signup.html')


def validate_test(test):
    if " " in test:
        return True
    else:
        if len(test) < 3 or len(test) > 20:
            return True
        else:
            return False


def validate_password(password, confirm_password):
    return (password == confirm_password)


def validate_email(email):
    if "@" and "." not in email:
        return True
    if len(email) > 20:
        return True
    else:
        return False


def input_blank(test):
    if test == '':
        return True
    else:
        return False


@app.route('/', methods=['POST'])
def validate_form():

    user_name = request.form['username']

    password = request.form['password']

    verify_password = request.form['verify_password']

    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    error_check = False

    if validate_test(user_name):
        username_error = "That's not a valid username"
        error_check = True

    if validate_test(password):
        password_error = "That's not a valid password"
        error_check = True

    if password != verify_password:
        verify_error = "Passwords don't match"
        error_check = True

    if email != '':
        if validate_email(email):
            email_error = "That's not a valid email"
            error_check = True

    if error_check == False:
        return redirect('/welcome?username={0}'.format(user_name))
    else:
        return render_template('/user_signup.html',
                               username_error=username_error, 
                               password_error=password_error, 
                               verify_error=verify_error, 
                               email_error=email_error,
                               username=user_name,
                               email=email)


@app.route("/welcome")
def welcome():

    user_name = request.args.get('username')

    return render_template('welcome.html', user_name=user_name)


app.run()
