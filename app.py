from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'addition':
        result = num1 + num2
        operation_symbol = '+'
    elif operation == 'subtraction':
        result = num1 - num2
        operation_symbol = '-'
    elif operation == 'multiplication':
        result = num1 * num2
        operation_symbol = '*'
    elif operation == 'division':
        result = num1 / num2
        operation_symbol = '/'

    return render_template('result.html', num1=num1, num2=num2, operation_symbol=operation_symbol, result=result)

if __name__ == '__main__':
    app.run(debug=True)
