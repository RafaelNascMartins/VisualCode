filmSet = {"Matrix", "Vingadores", "O Senhor dos Anéis", "Star Wars", "O Poderoso Chefão"}
print(type(filmSet))

# 1 - Buscar o tamanho do set
print(len(filmSet))

# 2 - True e 1 são considerados iguais em um set, assim como False e 0
setTeste = {"Matrix", True, 1, 8.7}
print(setTeste)
# True e 1 são retornados juntos, pois são considerados iguais em um set

# 3 - Adicionar um item de outro set
filmSet.update({"Harry Potter"})
print(filmSet)  

# 4 - Remover um item do set
filmSet.remove("Vingadores")
print(filmSet)  