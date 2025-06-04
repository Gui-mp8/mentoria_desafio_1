import requests
import json

def buscar_vagas(vaga: str):
    todas_as_vagas = []

    for _ in range(0, 100, 10):
        url = f"https://portal.api.gupy.io/api/job?name={vaga}&offset=0&limit=10"
        resposta = requests.get(url)

        print(f"Buscando vaga: {vaga}")
        print(f"Status code: {resposta.status_code}")
        print(f"Resposta: {resposta.text[:200]}")

        if resposta.status_code == 200:
            dados = resposta.json()

        todas_as_vagas.extend(dados.get("data", []))
    else:
        print(f"Erro ao buscar vaga '{vaga}': {resposta.status_code}")


    with open("./data/gupy.json", "w", encoding="utf-8") as f:
        json.dump(todas_as_vagas, f, indent=4, ensure_ascii=False)


