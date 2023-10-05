classificacaoPaulista2023 = (
    "Palmeiras", "Água Santa", "São Bernanrdo", "São Paulo",
    "Bragantino", "Corinthians", "Mirassol", "Guarani", "Botafogo", "Santo André"
)

primeirosTres = classificacaoPaulista2023[:3]
ultimosTres = classificacaoPaulista2023[-3:]
ordemAlfabetica = sorted(classificacaoPaulista2023)
timeBragantino = "Bragantino"
posicaoBragantino = classificacaoPaulista2023.index(timeBragantino) + 1

print("Os 3 primeiros colocados são:", primeirosTres)
print("Os 3 últimos colocados são:", ultimosTres)
print("Times em ordem alfabética:", ordemAlfabetica)
print(f"O {timeBragantino} está na posição {posicaoBragantino}")
