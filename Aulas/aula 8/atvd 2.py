from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Bem-vindo"

@app.route('/curso')
def curso():
    return "Desinvolvimento de Sistemas"

@app.route('/escola')
def escola():
    return "CEEP"

if __name__ == '__main__':
    app.run(debug=True)