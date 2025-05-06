from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2'])
        operator = request.form['operator']

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2 if num2 != 0 else 'Error: Divide by zero'
        else:
            result = 'Invalid operator'

        return str(result)
    except Exception as e:
        return f'Error: {str(e)}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
