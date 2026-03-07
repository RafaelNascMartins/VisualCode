filmsTupla = ('Star Wars', 'Matrix', 'Senhor dos Anéis')
print(type(filmsTupla))

#Tuplas são imutáveis, ou seja, não podem ser alteradas depois de criadas
#filmsTupla[0] = 'Star Trek' #Isso vai gerar um erro porque as tuplas não podem ser alteradas

# 1 - Buscar os dois primeiros itens da tupla
print(filmsTupla[0:2])

# 2 - Buscar o último item da tupla
print(filmsTupla[-1])

# 3 - Buscar filmes até uma determinada posição 
print(filmsTupla[:4])

# 4 - Buscar filmes a partir de uma determinada posição
print(filmsTupla[0:4])

# 5 = Recuperar um item da tupla pelo nome
print(filmsTupla.index('Matrix')) #Isso vai retornar o índice do item 'Matrix' na tupla

# 6 -  Recuperar o item mais parecido com o nome
# Não é possível recuperar um item mais parecido com o nome em uma tupla, pois as tuplas não possuem métodos de busca por similaridade. Para isso, seria necessário usar uma lista ou um dicionário, onde é possível implementar uma função de busca por similaridade.