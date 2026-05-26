import requests
import urllib.parse

def obter_previsao_completa(cidade, api_key):
    # Trata acentos e espaços na URL
    cidade_codificada = urllib.parse.quote(cidade)
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade_codificada}&appid={api_key}&units=metric&lang=pt_br"
    
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status() 
        dados = resposta.json()
        
        # Coleta os dados com segurança
        temperatura = dados.get('main', {}).get('temp', 'N/A')
        condicoes = dados.get('weather', [{}])[0].get('description', 'Sem descrição')
        humidade = dados.get('main', {}).get('humidity', 'N/A')
        
        # Retorna a string formatada para o print
        return (
            f"\n--- Clima em {cidade.title()} ---\n"
            f"Temperatura Atual: {temperatura}°C\n"
            f"Condição: {condicoes.capitalize()}\n"
            f"Umidade: {humidade}%"
        )
        
    except requests.exceptions.ConnectionError:
        return "Erro de conexão: Verifique sua internet."
    except requests.exceptions.HTTPError:
        return "Erro: Cidade não encontrada ou chave de API inválida."
    except Exception as err:
        return f"Erro inesperado: {err}"

# --- EXECUÇÃO ---
SUA_API_KEY = "SUA_CHAVE_AQUI" 
cidade_usuario = input("Digite o nome da cidade: ")
print(obter_previsao_completa(cidade_usuario, SUA_API_KEY))