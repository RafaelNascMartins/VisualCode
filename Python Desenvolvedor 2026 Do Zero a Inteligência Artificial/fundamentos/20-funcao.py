# 1 = Função para imprimir uma mensagem
def funcao():
    print("Olá, mundo!")

# for i in range(5):
#     funcao()

# 2 = Funcão para calcular a media de notas
def media():
    numNotas = int(input("Quantas notas deseja calcular? "))
    soma = 0
    for i in range(numNotas):
        nota = float(input(f"Digite a nota {i + 1}: "))
        soma += nota

    if numNotas > 0:
        media = soma / numNotas
    else:
        media = 0
    
    return media
print(f"A média das notas é {media():.2f}")

# 3 - Função para cadastrar um filme
def cadastrar_filme():
    tituloFilme = input("Digite o título do filme: ")
    diretorFilme = input("Digite o nome do diretor do filme: ")
    anoFilme = int(input("Digite o ano de lançamento do filme: "))
    generoFilme = input("Digite o gênero do filme: ")
    print(f"Filme cadastrado: {tituloFilme} ({anoFilme}), dirigido por {diretorFilme}, gênero: {generoFilme}")

cadastrar_filme()


    