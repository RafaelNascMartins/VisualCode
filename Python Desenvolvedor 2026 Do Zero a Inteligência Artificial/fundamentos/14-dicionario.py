filmPoderosoChefao = {
    "titulo": "O Poderoso Chefão",
    "diretor": "Francis Ford Coppola",
    "ano": 1972,
    "genero": ["Crime", "Drama"],
    "elenco": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"],
}
print(filmPoderosoChefao)
print(len(filmPoderosoChefao))
print(type(filmPoderosoChefao))

# 1 - Recuperar um elemento do dicionário
print(filmPoderosoChefao["elenco"][0])
print(filmPoderosoChefao.get("diretor"))

# 2 - Buscar apenas as chaves do dicionário
print(filmPoderosoChefao.keys()) #chaves seriam titulo, diretor, ano, genero, elenco neste caso

# 3 - Buscar apenas os valores do dicionário
print(filmPoderosoChefao.values()) #Vai retornar os valores do dicionário, ou seja, o título, diretor, ano, gênero e elenco, e todos os valores associados a essas chaves.

# 4 - Buscar itens do dicionário
print(filmPoderosoChefao.items()) #Vai retornar uma lista de tuplas, onde cada tupla contém uma chave e seu valor correspondente do dicionário. Por exemplo, a tupla ("titulo", "O Poderoso Chefão") representa a chave "titulo" e seu valor associado "O Poderoso Chefão".

# 5 - Adicionar um novo elemento ao dicionário
filmPoderosoChefao["duracao"] = "2 horas e 55 minutos"
print(filmPoderosoChefao)
# Mas e se ja existir a chave? Ele vai substituir o valor antigo pelo novo valor
filmPoderosoChefao["ano"] = 1974
# Ta.. mas e se eu quiser que NÃO substitua o valor antigo? Aí eu posso usar o método setdefault, que só vai adicionar a chave e valor se a chave não existir no dicionário
filmPoderosoChefao.setdefault("ano", 1974) #Como a chave "ano" já existe, ele não vai adicionar o valor 1974, e vai manter o valor antigo que é 1972, aqui utilizamos um set dentro do dicionario, assim deixando ele imutável.

# 6 - Atualizar um elemento do dicionário
filmPoderosoChefao.update({"diretor": "Francis Ford Coppola"})
print(filmPoderosoChefao)

# 7 - Remover um elemento do dicionário
filmPoderosoChefao.pop("duracao") #Remove a chave "duracao" #pop basicamente remove a chave e retorna o valor associado a ela, ou seja, "2 horas e 55 minutos" nesse caso.
print(filmPoderosoChefao)