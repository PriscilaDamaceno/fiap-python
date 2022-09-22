#lista vazia
lista = []
print(type(lista))
#lista com dados
lista = [2005, 2002, 1980, 1983, 1977, 1999]
#exibição de Lista completa
print(lista)
#exibição de uma posição especifica
print(lista[3])
#exibir intervalo da lista - sublista | se omitir o valor após os dois pontos ele vai
#do valor 2 até o final
print(lista[2:4])
#iteração de lista
for ano in lista:
    print(f"No ano de {ano} saiu um filme do Star Wars no cinema")
#inclusão de dados
lista.append(2022)
print(lista)
#inclusão de dados em um indice especifico da lista
lista.insert(2, 2000)
print(lista)

#remoção de um elemento em uma posição especifica
lista.pop(7)
print(lista)
#contagem de um determinado elemento na lista
print(lista.count(2000))
#inversão da lista
lista.reverse()
print(lista)
#ordenação de lista
lista.sort()
print(lista)
#contagem de elementos da lista
print(len(lista))