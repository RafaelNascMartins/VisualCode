# 1 - Fatorial de um número
# def fatoria(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero * fatoria(numero - 1)
# numeroConta = int(input('Digite um número para calcular o fatorial: \n'))
# print(f"O fatorial de {numeroConta} é: {fatoria(numeroConta)}")

# 2 - Soma total de um número
def totalSoma(num):
    if num == 1:
        return 1
    else:
        return num + totalSoma(num - 1)

num = int(input('Digite um número para calcular a soma total: \n'))
print(f"A soma total de {num} é: {totalSoma(num)}")