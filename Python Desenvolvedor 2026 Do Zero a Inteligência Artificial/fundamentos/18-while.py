# Lista de armas
from operator import index


armasFNV = ["Anti-Material Rifle", "10mm Pistol", "Combat Shotgun", "Plasma Rifle"]

# 1 - Iterando valores de uma lista de armas usando while
indice = 0
while indice < len(armasFNV):
    print(armasFNV[indice])
    indice += 1

# 2 - Quando a condição for atendida, o loop será encerrado
indice = 0
while indice < len(armasFNV):
    if armasFNV[indice] == "Combat Shotgun":
        break
    print(armasFNV[indice])
    indice += 1

# 3 = Quando a condição for atendida, o loop vai para próxima iteração
# indice = 0
# while indice < len(armasFNV):
#     if armasFNV[indice] == "Combat Shotgun":
#         index += 1
#         continue    
#     print(armasFNV[indice])
#     indice += 1

# 4 - Avaliação da filme com while
nomeFilme = input("Digite o nome do filme: ")
avaliacao = int(input("DIgite quantas avaliações deseja fazer:\n"))

total = 0 # Variável para armazenar a soma das avaliações
count = 0

while count < avaliacao:
    nota = float(input("Digite a nota do filme:\n"))
    total += nota
    count += 1

if avaliacao > 0:
    media = total / avaliacao
else:
    media = 0
print(f"A média de avaliação do filme '{nomeFilme}' é: {media:.1f}")