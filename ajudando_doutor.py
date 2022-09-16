email_aluno = input("Informe o e-mail do aluno: ")
nota_semestral = input("Informe a nota semestral: ")
nota_semestral = float(nota_semestral)
if nota_semestral > 8.5:
    print("Enviando o e-email para {}".format(email_aluno))
    