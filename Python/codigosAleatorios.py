rafael = "Rafael"
pedro = "pedro"
print(rafael)

qual_o_nome = input("Digite seu nome:")
if qual_o_nome == "Rafael":
    print("Olá, Admin!")
elif qual_o_nome != "Pedro":
    print("Olá, " + qual_o_nome + "!")
else:
    print("Olá, Pedro!")
