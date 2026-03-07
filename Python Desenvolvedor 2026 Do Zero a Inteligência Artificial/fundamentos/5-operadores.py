num1 = int(input("Digite o primeiro número: \n"))
num2 = int(input("Digite o segundo número: \n"))

# Operadores Aritméticos
sum = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2
divicao = num1 / num2
exp = num1 ** num2
restoDivisao = num1 % num2

print(f"A soma dos números {num1} e {num2} é: {sum}")
print(f"A subtração dos números é: {subtracao}")

#Comparação
maior = num1 > num2
menor = num1 < num2
igual = num1 == num2
diferente = num1 != num2
maiorIgual = num1 >= num2
menorIgual = num1 <= num2


print(f"O número {num1} é maior que o número {num2}? {maior}")
print(f"O número {num1} é menor que o número {num2}? {menor}")

# Atribuição
num1 += num2 # num1 = num1 + num2
print(f"O valor do num1 após a atribuição é: {num1}")