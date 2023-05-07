jogadores, partidas = input().split()
jogadores, partidas = int(jogadores), int(partidas)

mat = []
for i in range(jogadores):
    linha = []
    valores = input().split() #mais de uma entrada de dados por linha
    for j in range(partidas):
        linha.append(int(valores[j]))
    mat.append(linha)

gol = 0
for i in range(jogadores):
    if all(mat[i]):
        gol += 1

print(gol)

