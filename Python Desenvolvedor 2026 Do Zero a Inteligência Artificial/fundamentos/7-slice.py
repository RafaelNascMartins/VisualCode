movieName =  "O Poderoso Chefão"

#sting[inicio:fim:] = indice começa na posicao 0 / indice final é -1

# 1 - Buscar toda a string a partidar da primeira posicao
print(movieName[0:]) 

# 2 - Buscar toda a string a partidar da ultima posicao
print(movieName[:10])

# 3 - Buscar toda string da terceira até a última posição
print(movieName[2:])

print(movieName[0::-1]) # Inverte a string, ou seja, começa do final para o início

"""
string[início:fim:passo]
índice começa na posição 0 | índice final - 1
passo - determina o incremento. Por padrão esse número é o 1.
"""

# 4 - Buscar toda a string de 2 em 2 caracteres
print(movieName[::2])

