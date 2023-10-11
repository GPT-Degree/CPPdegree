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
        
       
        result = (num3 + num4 + 1800 ) - (num1 + num2)

        
        return redirect(url_for('result', result=result, num3=num3, num4=num4))
    except ValueError:
        return "Invalid input. Please enter valid numbers."


    

@app.route('/result/<result>/<int:num3>/<int:num4>')
def result(result, num3, num4):
    return render_template('result.html', result=result, num3=num3, num4=num4)

@app.route('/resources')
def resources():
    return render_template('resources.html',methods=['POST'])

@app.route('/cpp')
def cpp():
    return render_template('cpp.html',methods=['POST'])

@app.route('/csuf')
def csuf():
    return render_template('csuf.html',methods=['POST'])

@app.route('/csula')
def csula():
    return render_template('csula.html',methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
