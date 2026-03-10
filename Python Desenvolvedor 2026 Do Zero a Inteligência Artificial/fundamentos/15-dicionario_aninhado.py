import pprint

filmFlix = {
    "Poderoso Chefão": {
        "titulo": "O Poderoso Chefão",
        "diretor": "Francis Ford Coppola",
        "ano": 1972,
        "genero": ["Crime", "Drama"],
        "elenco": ["Marlon Brando", "Al Pacino", "James Caan", "Diane Keaton"]
    },
    "O Senhor dos Anéis": {
        "titulo": "O Senhor dos Anéis",
        "diretor": "Peter Jackson",
        "ano": 2001,
        "genero": ["Aventura", "Fantasia"],
        "elenco": ["Elijah Wood", "Ian McKellen", "Orlando Bloom"]
    }
}
pp = pprint.PrettyPrinter(depth=5)
pp.pprint(filmFlix)
# Deste jeito, podemos ter um dicionário dentro de outro dicionário, ou seja, um dicionário aninhado. Isso é útil para organizar informações de forma hierárquica, como no caso de um catálogo, ou pensando em um banco de dados com diversos diretórios.

# 1 - Buscar uma informação específica dentro do dicionário aninhado
print(filmFlix["Poderoso Chefão"]["diretor"]) #Vai retornar o diretor do filme "O Poderoso Chefão", que é "Francis Ford Coppola".

# 2 - Adicionar novo item
filmFlix["Poderoso Chefão"]["comentarios"] = ["Excelente filme!", "Clássico do cinema!"]
pp.pprint(filmFlix["Poderoso Chefão"])

# 3 - Excluir um dicionário 
del filmFlix["O Senhor dos Anéis"]
pp.pprint(filmFlix)