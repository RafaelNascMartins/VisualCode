# 1 = Função que imprime um nome completo
def nome_completo(nome, sobrenome):
    print(f"Nome completo: {nome} {sobrenome}")

nome_completo("João", "Silva")
nome_completo("Maria", "Santos")

# 2 = Função para somar dois números
def  somaNumeros(num1, num2):
    return num1 + num2

print(f"A soma de 5 e 3 é: {somaNumeros(5, 3)}")
print(f"A soma de 10 e 20 é: {somaNumeros(10, 20)}")

# 3 - Função com parâmetro default
def endereco(pais="Brasil"):
    print(f"Eu moro em: {pais}")

endereco() # Usa o valor default "Brasil"
endereco("Argentina") # Sobrescreve o valor default com "Argentina"

# 4 - Função para avaliar um filme
def avaliarFilme(numeroDeRatings, nomeFilme):
    total = 0
    for i in range(numeroDeRatings):
        rating = float(input(f"Digite a avaliação {i + 1} para o filme '{nomeFilme}': "))
        total += rating
    if numeroDeRatings > 0:
        media = total / numeroDeRatings
    else:
        media = 0
    
    print(f"A média de avaliações para o filme '{nomeFilme}' é: {media:.2f}")

avaliarFilme(2, "Sonic")