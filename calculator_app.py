from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Codecademy Calculator!"

# Get numbers from the user
num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))

@app.route('/division')
def division():
    return f"Now dividing {num1} and {num2}! The result is: {num1 / num2}"

@app.route('/multiplication')
def multiplication():
    return f"Now multiplying {num1} and {num2}! The result is: {num1 * num2}"

@app.route('/addition')
def addition():
    return f"Now adding {num1} and {num2}! The result is: {num1 + num2}"

@app.route('/subtraction')
def subtraction():
    return f"Now subtracting {num1} and {num2}! The result is: {num1 - num2}"

@app.route('/power')
def power():
    return f"Now raising {num1} to the power of {num2}! The result is {num1 ** num2}"

if __name__ == '__main__':
    app.run(debug=True)
