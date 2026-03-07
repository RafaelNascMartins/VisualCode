movieName = "O Poderoso Chefão"
movieName2 = "o poderoso chefão"
print(movieName == movieName2) # Case sensitive

descricaoFilme = """
O Poderoso Chefão é um filme de 1972 dirigido por Francis Ford Coppola e baseado no romance homônimo de Mario Puzo. O filme é considerado um dos maiores clássicos do cinema e é conhecido por sua narrativa envolvente, personagens complexos e atuações memoráveis.
"""

print(movieName.upper()) # Transforma a string em maiúscula
print(movieName.lower()) # Transforma a string em minúscula
print(movieName.title()) # Transforma a primeira letra de cada palavra em maiúscula
print(movieName.capitalize()) # Transforma a primeira letra da string em maiúscula e o restante em minúscula
print(movieName.center(10, '-')) # Centraliza a string e preenche os espaços com o caractere especificado
print(movieName.find("Chefão")) # Retorna o índice da primeira ocorrência da substring, ou -1 se não for encontrada
print(movieName.count("o")) # Retorna o índice da primeira ocorrência da letra "o"
print(movieName.replace("Poderoso chefão", "Game of Thrones")) # Substitui a substring por outra string
print(movieName.split()) # Divide a string em uma lista de palavras