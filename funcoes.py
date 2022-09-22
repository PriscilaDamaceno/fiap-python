#Função sem return
def saudacao_noturna():
    print("Boa noite!")
saudacao_noturna()

#Função com argumentos
def saudacao(nome):
    print(f"Boa noite, {nome}")
nomes = ["Priscila", "Sayori", "Pedro"]
for nome in nomes:
    saudacao(nome)

#Função com return
def saudacao_return(nome):
    return f"Boa noite, {nome}"
