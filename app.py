from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    try:
        num1 = int(request.form['num1']) #financial aid section
        num2 = int(request.form['num2']) #scholarship section
        num3 = int(request.form['housing']) #housing section
        num4 = int(request.form['credits']) #credits section
        
       
        result = (num3+ num4) - (num1 + num2)

        
        return redirect(url_for('result', result=result))
    except ValueError:
        return "Invalid input. Please enter valid numbers."


    

@app.route('/result/<result>')
def result(result):
    return render_template('result.html', result=result)

@app.route('/resources')
def resources():
    return render_template('resources.html',methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
