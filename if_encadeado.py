rm = input("Insira seu RM: ")
nome = input("Insira seu nome: ")
idade = input("Insira sua idade: ")
email = input("Insira seu e-mail: ")
if int(idade) >= 18:
    print("{} sua participação foi autorizada, aluno de RM {}!".format(nome, rm))
    print("Mais informações serão enviadas em breve para o e-mail: {}".format(email))
else:
    autorizado = input("{}, você possui autorização do responsável? - Por favor digite S-Sim ou N-Não: ".format(nome))
if autorizado == 'S':
    print("{}, sua participação foi liberada, em breve entraremos em contato através do e-mail: {}. Boa sorte".format(nome, email))
else:
    print("{},sua participação não foi autorizada, sinto muito".format(nome))