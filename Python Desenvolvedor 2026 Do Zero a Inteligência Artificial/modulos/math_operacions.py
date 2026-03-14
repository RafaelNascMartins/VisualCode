# Módulo de operações mátematicas

def soma(a, b):
    return a + b
def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Não é possível a divisão por 0")


 