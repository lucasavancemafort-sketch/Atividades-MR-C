from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route('/saudacao')
def saudacao():
    return "Olá! Seja bem-vindo!"

@app.route('/data')
def data():
    return f"Data de hoje: {date.today()}"

if __name__ == '__main__':
    app.run(debug=True)