# #Informações sobre o filme
# name = input("Digite o nome do filme: ")
# anoLancamento = int(input("Digite o ano de lançamento do filme: "))
# rating = float(input("Digite a avaliação do filme: "))

# # Verifica se o filme é recomendado
# if rating > 8.0 and anoLancamento > 2000:
#     print(f"O filme '{name}' é muito bom, recomendo assisti-lo.")
# else:
#     print(f"não assista essa bosta")

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    result = num1 + num2
elif operacao == "-":
    result = num1 - num2
elif operacao == "*":
    result = num1 * num2
elif operacao == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Erro: Divisão por zero não é permitida."
else:
    result = "Operação inválida."
print(f"O resultado da operação é: {result:.1f}")