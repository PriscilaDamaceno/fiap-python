#fazer uma lista de convidados numa festa
#no final deve exibir a quantidade de convidados que apareceram,
#e a ordem de chegada

resposta = "SIM"
convidados = []
while resposta.upper() != "NÃO":
    nome_convidado = input("Informe o nome do convidado: ")
    convidados.append(nome_convidado)
    resposta = input("Deseja informar mais convidados? SIM OU NÃO?")

print(f"Compareceram{len(convidados)} convidados!\n")
print(f"Ordem de chegada dos convidados: ")
for convidado in convidados:
    print(convidado)

    convidados.sort()
    print(f"\nOrdem alfabética dos convidados:")
    for convidado in convidados:
        print(convidado)