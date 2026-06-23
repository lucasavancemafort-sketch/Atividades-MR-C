from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Notebook Dell", "preco": 4500.00, "disponivel": True},
    {"id": 2, "nome": "Mouse Logitech", "preco": 89.90, "disponivel": True},
    {"id": 3, "nome": "Teclado Mecânico", "preco": 299.90, "disponivel": False},
    {"id": 4, "nome": "Monitor 24 polegadas", "preco": 899.90, "disponivel": True}
]

@app.route('/produtos/disponiveis')
def produtos_disponiveis():
    disponiveis = []
    for produto in produtos:
        if produto["disponivel"] == True:
            disponiveis.append(produto)
    return jsonify(disponiveis)

if __name__ == '__main__':
    app.run(debug=True)