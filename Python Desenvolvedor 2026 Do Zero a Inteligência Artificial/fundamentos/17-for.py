# Lista de filmes
listaFilmes = ["O Poderoso Chefão", "Pulp Fiction", "Clube da Luta", "Forrest Gump", "Matrix"]
armasFNV = ["Anti-Material Rifle", "10mm Pistol", "Combat Shotgun", "Plasma Rifle", "Gauss Rifle"]

# print(listaFilmes)
# 1 - Iterando valores de uma lista
for filmes in listaFilmes:
    print(filmes)

# 2 - Quando a condição for atendida, o loop será encerrado
for armas in armasFNV:
    if armas == "Combat Shotgun":
        break
    print(armas)

# 3 - Quando a condição for atendida, o loop irá pular para a próxima iteração
for armas in armasFNV:
    if armas == "Plasma Rifle":
        continue
    print(armas)

# 4 = Avaliação do filme
nomeFilme = input("Digite o nome do filme: ")
avaliacao = int(input("DIgite quantas avaliações deseja fazer:\n"))

total = 0 # Variável para armazenar a soma das avaliações
for i in range(avaliacao):
    nota = float(input("Digite a nota do filme:\n"))
    total += nota

if avaliacao > 0:
    media = total / avaliacao
else:
    media = 0
print(f"A média de avaliação do filme '{nomeFilme}' é: {media:.1f}")

#Exercicio para fixar, tema de Fallout New vegas
cassinos = int(input("Quantos cassinos você visitou?\n"))
totalDeCaps = 0
for i in range(cassinos):
    caps = int(input("Quantos caps você ganhou nesse cassino?\n"))
    totalDeCaps += caps
if cassinos == 0:
    print("Sem gasto, sem dinheiro")
else:    
    mediaCaps = totalDeCaps / cassinos  
    print(f"A quantidade de Caps que você ganhou foi: {totalDeCaps} e a média de caps ganhos por cassino é: {mediaCaps:.1f}")

# 2 - Exercicio 2 para fixar, tema de Fallout New vegas
inimigos = int(input("Quantos inimigos você derrotou?\n"))
totalDeInimigos = 0
lootRaro = 0
capsTotal = 0

for i in range(inimigos):
    caps = int(input(f"Quantos caps o inimigo {i+"texto"} deixou?\n"))
    capsTotal += caps
    if caps >= 50:
        lootRaro += 1
print(f"você encontrou {capsTotal} caps e também {lootRaro} itens raros!")

