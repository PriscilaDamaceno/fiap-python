opcao = 0

while opcao != 3:
    print("Menu firmeza!")
    print("1-Receber um elogio")
    print("2- Frase motivacional")
    print("3- sair ")
    opcao = int(input("Informe sua opção: "))

    if opcao == 1:
        print("Lindissimo!")

    elif opcao ==2:
        print("Nada é tão ruim que não possa piorar")

    elif opcao ==3:
        print("Tchau!")

    else:
        print("Tá errado animal!")