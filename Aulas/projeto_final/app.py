import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)
DATABASE = "banco.db"


def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS categorias (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    """
    )

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS piadas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pergunta TEXT NOT NULL,
            resposta TEXT NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY (categoria_id) REFERENCES categorias (id) ON DELETE CASCADE
        )
    """
    )

    conn.commit()
    conn.close()


init_db()

@app.route("/categorias", methods=["GET"])
def get_categorias():
    conn = get_db_connection()
    categorias = conn.execute("SELECT * FROM categorias").fetchall()
    conn.close()
    return jsonify([dict(c) for c in categorias]), 200


@app.route("/categorias/<int:id>", methods=["GET"])
def get_categoria(id):
    conn = get_db_connection()
    categoria = conn.execute(
        "SELECT * FROM categorias WHERE id = ?", (id,)
    ).fetchone()
    conn.close()

    if categoria is None:
        return jsonify({"erro": "Categoria não encontrada"}), 404

    return jsonify(dict(categoria)), 200


@app.route("/categorias", methods=["POST"])
def create_categoria():
    dados = request.get_json()

    if not dados or "nome" not in dados or not dados["nome"].strip():
        return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO categorias (nome) VALUES (?)", (dados["nome"].strip(),)
    )
    conn.commit()
    novo_id = cursor.lastrowid
    conn.close()

    return jsonify({"id": novo_id, "nome": dados["nome"].strip()}), 201


@app.route("/categorias/<int:id>", methods=["PUT"])
def update_categoria(id):
    dados = request.get_json()

    if not dados or "nome" not in dados or not dados["nome"].strip():
        return jsonify({"erro": "O campo 'nome' é obrigatório"}), 400

    conn = get_db_connection()
    cursor = conn.cursor()

    categoria = cursor.execute(
        "SELECT * FROM categorias WHERE id = ?", (id,)
    ).fetchone()
    if categoria is None:
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 404

    cursor.execute(
        "UPDATE categorias SET nome = ? WHERE id = ?",
        (dados["nome"].strip(), id),
    )
    conn.commit()
    conn.close()

    return jsonify({"id": id, "nome": dados["nome"].strip()}), 200


@app.route("/categorias/<int:id>", methods=["DELETE"])
def delete_categoria(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    categoria = cursor.execute(
        "SELECT * FROM categorias WHERE id = ?", (id,)
    ).fetchone()
    if categoria is None:
        conn.close()
        return jsonify({"erro": "Categoria não encontrada"}), 404

    cursor.execute("DELETE FROM categorias WHERE id = ?", (id,))
    conn.commit()
    conn.close()

    return (
        jsonify({"mensagem": "Categoria e piadas associadas deletadas com sucesso"}),
        200,
    )


@app.route("/piadas", methods=["GET"])
def get_piadas():
    conn = get_db_connection()
    piadas = conn.execute("SELECT * FROM piadas").fetchall()
    conn.close()
    return jsonify([dict(p) for p in piadas]), 200


@app.route("/piadas/<int:id>", methods=["GET"])
def get_piada(id):
    conn = get_db_connection()
    piada = conn.execute("SELECT * FROM piadas WHERE id = ?", (id,)).fetchone()
    conn.close()

    if piada is None:
        return jsonify({"erro": "Piada não encontrada"}), 404

    return jsonify(dict(piada)), 200


