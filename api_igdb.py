
import requests
import random
import time


# 1. Obter token OAuth da Twitch

def get_token(client_id, client_secret):
    url = "https://id.twitch.tv/oauth2/token"
    payload = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials"
    }

    response = requests.post(url, data=payload)
    data = response.json()
    return data["access_token"]


# 2. Buscar 111 jogos aleatórios

def buscar_111_jogos(client_id, token):
    url = "https://api.igdb.com/v4/games"

    headers = {
        "Client-ID": client_id,
        "Authorization": f"Bearer {token}"
    }

    jogos = []

    for _ in range(15):
        offset = random.randint(0, 200000)

        query = (
            "fields id,name,rating,genres,themes; "
            f"limit 50; offset {offset};"
        )

        r = requests.post(url, data=query, headers=headers)

        if r.status_code == 200:
            jogos.extend(r.json())

        time.sleep(0.2)

    random.shuffle(jogos)
    return jogos[:111]


# 3. Converter para o formato do arquivo jogos.py

def converter(jogo):
    nome = jogo.get("name", "Sem Nome")
    rating = int(jogo.get("rating", 0))

    generos = {f"genero_{g}" for g in jogo.get("genres", [])}
    temas = {f"tema_{t}" for t in jogo.get("themes", [])}
    players = {"single"} 

    return nome, rating, generos, temas, players



# 4. Gerar ARQUIVO PYTHON com a lista dos 111 jogos

def salvar_arquivo(lista_convertida):
    with open("jogos_gerados.py", "w", encoding="utf-8") as f:
        f.write("# Lista de 111 jogos gerados automaticamente via IGDB\n\n")

        for i, jogo in enumerate(lista_convertida):
            nome, rating, generos, temas, players = jogo

            nome_var = "jogo" + str(i + 1)

            f.write(f'{nome_var} = ["{nome}", {rating}, '
                    f"{generos}, {temas}, {players}]\n")

        f.write("\n\n# Lista geral\n")
        f.write("jogos = [\n")
        for i in range(750):
            f.write(f"    jogo{i+1},\n")
        f.write("]\n")

    print("[OK] Arquivo jogos_gerados.py criado com sucesso!")


# 5. MAIN

if __name__ == "__main__":
    CLIENT_ID = "COLOQUE_AQUI"
    CLIENT_SECRET = "COLOQUE_AQUI"

    print("Obtendo token...")
    token = get_token(CLIENT_ID, CLIENT_SECRET)

    print("Coletando jogos...")
    brutos = buscar_111_jogos(CLIENT_ID, token)

    print("Convertendo dados...")
    convertidos = [converter(j) for j in brutos]

    print("Gerando arquivo jogos_gerados.py...")
    salvar_arquivo(convertidos)
