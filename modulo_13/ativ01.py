# Configure um servidor Flask básico com uma rota GET /saudacao.

from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/saudacao', methods=['GET'])
def saudacao():
    return jsonify({'mensagem': 'Olá, seja bem-vindo ao curso de EAD!'})
if __name__ == '__main__':
    app.run(debug=True)

# Crie uma rota POST /cadastrar para receber dados de usuário via JSON.
from flask import Flask, jsonify, request
app = Flask(__name__)
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    return jsonify({'mensagem': f'Usuário {nome} com email {email} cadastrado com sucesso!'})
if __name__ == '__main__':
    app.run(debug=True)

# Conecte-se ao SQLite para persistir dados de usuários em um babco de dados.
import sqlite3
from flask import Flask, jsonify, request
app = Flask(__name__)
def init_db():
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = request.get_json()
    nome = data.get('nome')
    email = data.get('email')
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', (nome, email))
    conn.commit()
    conn.close()
    return jsonify({'mensagem': f'Usuário {nome} com email {email} cadastrado com sucesso!'})
if __name__ == '__main__':
    init_db()
    app.run(debug=True)

    