# Desenvolva uma API completa para um blog, com funcionalidades como criação de posts, gerenciamento de comentários e autenticação de usuários.
from flask import Flask, jsonify, request
app = Flask(__name__)
# Rota para criar um post
@app.route('/posts', methods=['POST'])
def criar_post():
    data = request.get_json()
    titulo = data.get('titulo')
    conteudo = data.get('conteudo')
    return jsonify({'mensagem': f'Post "{titulo}" criado com sucesso!'})
# Rota para adicionar um comentário a um post
@app.route('/posts/<int:post_id>/comentarios', methods=['POST'])
def adicionar_comentario(post_id):
    data = request.get_json()
    comentario = data.get('comentario')
    return jsonify({'mensagem': f'Comentário adicionado ao post {post_id} com sucesso!'})
# Rota para autenticação de usuários
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if username == 'admin' and password == 'senha123':
        return jsonify({'mensagem': 'Login bem-sucedido!'})
    else:
        return jsonify({'mensagem': 'Credenciais inválidas.'}), 401 
if __name__ == '__main__':
    app.run(debug=True)

