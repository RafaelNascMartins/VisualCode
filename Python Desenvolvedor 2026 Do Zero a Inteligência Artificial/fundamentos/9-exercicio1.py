#Ex.1

#primeiroNome: str = input("Qual seu nome? ")
#sobrenome: str = input("Qual seu sobrenome? ")

#nomeFormal = f"{sobrenome} {primeiroNome}"
#print(f"Olá {nomeFormal}, seja bem-vindo ao curso de Python!")
  
#Ex.2
#texto = "Python é muito legal!"
#palavras = texto.split() # O método split() divide a string em uma lista de palavras, usando o espaço como separador por padrão
#textoInvertido = " ".join(palavras[::-1]) # O método join() junta os elementos de uma lista em uma string, usando o espaço como separador. O slice [::-1] inverte a ordem da lista
#print(textoInvertido)

#Ex.3
texto1 = "arara"
texto2 = "python"

# Remove espaços em branco e converte para minúsculas
texto1Formatado = texto1.strip().lower() # O método strip() remove os espaços em branco no início e no final da string, e o método lower() converte a string para minúsculas
texto2Formatado = texto2.strip().lower()

# Verifica se o texto é um palíndromo
if texto1Formatado == texto1Formatado[::-1]: # O slice [::-1] inverte a string
    print(f"{texto1} é um palíndromo.")
else:    print(f"{texto1} não é um palíndromo.")
if texto2Formatado == texto2Formatado[::-1]:
    print(f"{texto2} é um palíndromo.")
else:    print(f"{texto2} não é um palíndromo.")