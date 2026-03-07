filmLista = ["Meia noite em paris", "Batman: Returns",
             "O Poderoso chefão", "O Senhor dos Anéis: O Retorno do Rei", "Pulp Fiction"]

# 1 - Tamanho da lista
print(len(filmLista))

# 2 - Recuperar um item da lista pelo índice
print(filmLista.index("O Poderoso chefão"))

# 3 - Adicionar um item à lista
filmLista.append("O Senhor dos Anéis: A Sociedade do Anel")
print(filmLista)

# 4 - Ordenar a lista
filmLista.sort()
print(filmLista)

# 5 - Copiar os itens de uma lista para outra
filmesCopia = filmLista.copy()
filmesCopia.remove("O Senhor dos Anéis: O Retorno do Rei")
print(filmesCopia)
print(filmLista)

# 6 - Remove todos os intens de da lista
filmesCopia.clear()
print(filmesCopia)

# 7 - Adionar um item em uma posição específica da lista
filmLista.insert(2, "Harry Potter e a Pedra Filosofal")
print(filmLista)

# 8 - Somar os itens de uma lista
numeros = [1, 2, 3, 4, 5]
print(sum(numeros))