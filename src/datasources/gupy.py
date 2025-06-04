import requests
import json

from typing import Any, Dict

Json_fisico = Dict[str, Any]

def finding_jobs(role: str, file_path: str) -> Json_fisico:
    all_jobs = []

    for _ in range(0, 100, 10):
        url = f"https://portal.api.gupy.io/api/job?name={role}&offset=0&limit=10"
        response = requests.get(url)

        print(f"Buscando vaga: {role}")
        print(f"Status code: {response.status_code}")
        print(f"Resposta: {response.text[:200]}")

        if response.status_code != 200:
            data = response.json()

        all_jobs.extend(data.get("data", []))
    else:
        print(f"Erro ao buscar vaga '{role}': {response.status_code}")


    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(all_jobs, f, indent=4, ensure_ascii=False)


