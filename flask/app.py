from flask import Flask, request, render_template

app = Flask(__name__)

# Define a route for the HTML form
@app.route('/')
def index():
    return render_template('index.html')

# Define a route to handle the addition
@app.route('/add', methods=['POST'])
def add():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        result = num1 + num2
        return render_template('result.html', result=result)
    except ValueError:
        return "Invalid input. Please enter valid numbers."

if __name__ == '__main__':
    app.debug = True
    app.run()
