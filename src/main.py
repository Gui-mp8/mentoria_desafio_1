from datasources.gupy import finding_jobs


def main():
    vagas = [
        "dados"
    ]

    for vaga in vagas:
        finding_jobs(vaga)

if __name__ == "__main__":
    main()
