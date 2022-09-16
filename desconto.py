valor_compra = input("Informe o valor da compra: ")
cupom= input("Digite o cupom de desconto: ")

if cupom == "NIVER10":
    valor_final = float(valor_compra) * 0.9
else:
    valor_final = float(valor_compra)
    print("Cupom inválido!")

    print("O valor final da compra é: {}".format(valor_final))
