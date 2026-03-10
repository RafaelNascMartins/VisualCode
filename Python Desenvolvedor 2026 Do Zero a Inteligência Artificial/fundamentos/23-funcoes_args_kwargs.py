""""
*Args = Utilizamos ele quando não temos certeza de quantos argumentos serão passados para a função, ou seja, quando queremos criar uma função que possa receber um número indeterminado de argumentos. Ele é representado por um asterisco (*) antes do nome do parâmetro.
- Os argumentos são passados para a função como uma tupla, e podemos acessá-los usando um loop ou indexação.
**kwargs = Além de valores podemos passar também as respectivas chaves para cada argumento
"""
def soma(*num):
    somaTotal = 0
    for n in num:
        somaTotal += n
    print(f"A soma total é: {somaTotal}")

soma(7, 3, 5, 2) #Posso ter a quantiade de argumentos que eu quiser, sem importar quantos ele pede, ele vai somar todos os argumentos que eu passar.
soma(4, 10, 9, 10, 14)

# 2 - Apresentação de cursos
def apresentacao(**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("Lista de Cursos")
apresentacao(name="Python", category="Backend", level="Iniciante")
apresentacao(name="Visão computacional com Python", category="IA", level="Avançado")
apresentacao(name="Dashboards com Dash", category="Ciencia de dados", level="Intermediario")