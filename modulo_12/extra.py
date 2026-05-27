from flask import Flask, jsonify, request
import pytest

app = Flask(__name__)

@app.route('/soma', methods=['POST'])
def soma():
    data = request.get_json()
    
    # CORREÇÃO: Valida se o corpo da requisição é um JSON válido
    if not data:
        return jsonify({'erro': 'O corpo da requisição deve ser um JSON válido.'}), 400
        
    a = data.get('a')
    b = data.get('b')
    
    # CORREÇÃO: Valida se os campos 'a' e 'b' foram enviados
    if a is None or b is None:
        return jsonify({'erro': 'Os parâmetros "a" e "b" são obrigatórios.'}), 400
        
    # CORREÇÃO: Valida se os valores enviados são numéricos (int ou float)
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return jsonify({'erro': 'Os parâmetros "a" e "b" devem ser números.'}), 400

    return jsonify({'resultado': a + b})


# ==========================================
# TESTES USANDO PYTEST
# ==========================================

@pytest.fixture
def client():
    # O test_client do Flask simula requisições HTTP sem subir o servidor real
    with app.test_client() as client:
        yield client    

# --- Testes de Caminho Feliz (Sucesso) ---

def test_soma(client):
    response = client.post('/soma', json={'a': 2, 'b': 3})
    assert response.status_code == 200
    assert response.get_json()['resultado'] == 5   

def test_soma_negativa(client):
    response = client.post('/soma', json={'a': -2, 'b': -3})
    assert response.status_code == 200
    assert response.get_json()['resultado'] == -5

def test_soma_zero(client):
    response = client.post('/soma', json={'a': 0, 'b': 0})
    assert response.status_code == 200
    assert response.get_json()['resultado'] == 0

# --- Testes de Entradas Inválidas (Validação de Erros) ---

def test_soma_valores_ausentes(client):
    """Testa o envio de um JSON incompleto (faltando o 'b')"""
    response = client.post('/soma', json={'a': 5})
    assert response.status_code == 400
    assert 'erro' in response.get_json()

def test_soma_valores_nao_numericos(client):
    """Testa o envio de strings em vez de números"""
    response = client.post('/soma', json={'a': 'dois', 'b': 3})
    assert response.status_code == 400
    assert response.get_json()['erro'] == 'Os parâmetros "a" e "b" devem ser números.'

def test_soma_json_vazio(client):
    """Testa o envio de uma requisição sem corpo JSON"""
    response = client.post('/soma', data="Não é um JSON")
    assert response.status_code == 415  # <-- Alterado aqui para 415