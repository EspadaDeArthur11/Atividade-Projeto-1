
import requests
import time


class TwitchIGDB:
 

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token = None
        self.expires_at = 0


    # 1. Pegando TOKEN OAuth (obrigatório para usar o IGDB)

    def get_token(self):
        if self.access_token and time.time() < self.expires_at:
            return self.access_token

        url = "https://id.twitch.tv/oauth2/token"
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "grant_type": "client_credentials",
        }

        response = requests.post(url, data=payload)
        data = response.json()

        self.access_token = data["access_token"]
        self.expires_at = time.time() + data["expires_in"]

        print("[OK] Token OAuth obtido com sucesso.")
        return self.access_token


    # 2. Buscar jogos por nome no IGDB
 
    def buscar_jogo(self, nome: str):
        token = self.get_token()

        url = "https://api.igdb.com/v4/games"
        headers = {
            "Client-ID": self.client_id,
            "Authorization": f"Bearer {token}",
        }

        query = f'search "{nome}"; fields name, rating, genres, summary; limit 5;'

        response = requests.post(url, data=query, headers=headers)

        if response.status_code != 200:
            print("Erro:", response.text)
            return None

        return response.json()
