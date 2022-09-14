rm = input("Insira seu RM: ")
idade = input("Insira sua idade: ")
if int(idade) >=18:
    print("Sua participação foi autorizada, aluno do RM {}!".format(rm))
    print("Mais informações serão enviadas para seu e-mail cadastrado!")
else:
    print("Você é menor de idade e não tem autorização para acessar a plataforma")
