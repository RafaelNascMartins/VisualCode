movieName = "O Poderoso Chefão"
movieName2 = "o poderoso chefão"
print(movieName == movieName2) # Case sensitive

descricaoFilme = """
O Poderoso Chefão é um filme de 1972 dirigido por Francis Ford Coppola e baseado no romance homônimo de Mario Puzo. O filme é considerado um dos maiores clássicos do cinema e é conhecido por sua narrativa envolvente, personagens complexos e atuações memoráveis.
"""
print(movieName)
line = "="
print(line * len(movieName)) # Len conta a quantidade de caracteres da string, incluindo espaços e pontuação
print(descricaoFilme)

# 2 - Procurar uma palavra dentro de uma string
print("Mario" in descricaoFilme)
if "Mario" in descricaoFilme:
    print("A palavra 'Mario' está presente na descrição do filme.")
else:
    print("A palavra 'Mario' não está presente na descrição do filme.")
# O operador in retorna um booleano, ou seja, True ou False
