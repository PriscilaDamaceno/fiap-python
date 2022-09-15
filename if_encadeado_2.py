pontuacao = int(input("Informe a pontuação: "))

if pontuacao > 1000:
    print("Você ganhou 3GB de bônus!")
elif pontuacao >500:
    print("Você ganhou 1,5GB de bônus")
elif pontuacao > 200:
    print("Você ganhou 500MB de bônus")
else:
    print("Você ainda não ganhou, mas continue juntando e volte novamente!")