# Função de potência de um número
power = lambda num: num ** 2

# Função que verifica se o número é par
ePar = lambda x: x % 2 == 0

# Função que divide um número por outro

div_num = lambda x, y: x / y

# Função que inverte uma string 
reversaoString = lambda s: s[ ::-1]

print(power(5))
print(power(9))
print(ePar(27))
print(ePar(30))
print(div_num(10, 2))
print(reversaoString("Python"))
print(reversaoString("JavaScript"))

# Funcionalidades relacionadas aos filmes:
listFilmes = ["Titanic", "O Poderoso Chefão", "Inception", "Jurassic Park", "Matrix"]
ratings = {
    "Titanic": [4.6, 9.0, 7.6],
    "O Poderoso Chefão": [7.5, 6.8, 8.6],
    "Inception": [3.3, 8.5, 7.5],
    "Jurassic Park": [4.2, 6.9, 6.7],
    "Matrix": [9.1, 7.4, 6.3]
}

# Função para calcular a média de avaliações de um filme
mediaRating = lambda movie_name: sum(ratings[movie_name]) / len(ratings[movie_name])

print(f"A média de Avaliações do filme Matrix é: {round(mediaRating('Matrix'), 2)}")
