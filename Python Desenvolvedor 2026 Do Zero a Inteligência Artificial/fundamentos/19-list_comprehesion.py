# 1 - Listando valores de 0 - 10 que sejam menores do que 4
listNumeros = [i for i in range(10) if i < 4]
print(listNumeros)

# Lista de filmes
listaFilmes = ["O Poderoso Chefão", "Pulp Fiction", "Clube da Luta", "Forrest Gump", "Matrix"]

# 2 - Listando os filmes que possuem a letra "a" em seu nome
filmeComA = [filme for filme in listaFilmes if 'a' in filme.lower()]
print(filmeComA)

# 3 - Filmes que eu assisti
filmesAssistidos = [filme for filme in listaFilmes if filme != "Clube da Luta"]

# 4 - Encontrando um filme nome
while True:
    procurarNome = input("Digite o nome do filme para busca-lo na lista (ou sair para encerrar)\n")
    if procurarNome.lower() == "sair":
        print("Programa Encerrado")
        break 

    filmesEncontrados = [filme for filme in listaFilmes if procurarNome.lower() in filme.lower()]
    if filmesEncontrados:
        print(f"Filmes encontrados com o nome: {procurarNome}:")
        for filmesEncontrado in filmesEncontrados:
            print(filmesEncontrado)
    else:
        print(f"Nenhum filme foi encontrado com o nome {procurarNome}. Tente novamente!")