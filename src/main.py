from datasource.endpoint.gupy import buscar_vagas


def main():
    vagas = [
        "dados"
    ]

    for vaga in vagas:
        buscar_vagas(vaga)

if __name__ == "__main__":
    main()
