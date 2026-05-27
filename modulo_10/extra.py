import requests

def obter_dados_filme(titulo, api_key):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={titulo}&language=pt-BR"
    
    mapeamento_generos = {
        28: "Ação", 12: "Aventura", 16: "Animação", 35: "Comédia", 80: "Crime",
        99: "Documentário", 18: "Drama", 10751: "Família", 14: "Fantasia",
        36: "História", 27: "Terror", 10402: "Música", 9648: "Mistério",
        10749: "Romance", 878: "Ficção Científica", 10770: "Cinema TV",
        53: "Suspense", 10752: "Guerra", 37: "Faroeste"
    }
    
    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()
        
        if dados.get('results'):
            filme = dados['results'][0]
            titulo_filme = filme.get('title', 'Sem título')
            genero_ids = filme.get('genre_ids', [])
            
            # Valida se a sinopse existe e não está vazia
            sinopse = filme.get('overview', '').strip()
            if not sinopse:
                sinopse = "Sinopse não disponível em português."
            
            # Traduz os gêneros
            nomes_generos = [mapeamento_generos.get(id, "Outro") for id in genero_ids]
            generos_formatados = ", ".join(nomes_generos) if nomes_generos else "Não informado"
            
            return (
                f"\n--- Informações do Filme ---\n"
                f"Título: {titulo_filme}\n"
                f"Gêneros: {generos_formatados}\n"
                f"Sinopse: {sinopse}"
            )
        else:
            return "Nenhum filme encontrado com esse título."
            
    except requests.exceptions.HTTPError:
        return "Erro: Falha na requisição. Verifique sua chave de API."
    except Exception as err:
        return f"Erro: {err}"

# --- EXECUÇÃO ---
SUA_API_KEY = "SUA_CHAVE_AQUI"
titulo_usuario = input("Digite o título do filme: ")
print(obter_dados_filme(titulo_usuario, SUA_API_KEY))