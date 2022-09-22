#O primeiro numero dentro do parenteses é onde começa o loop,
# o segundo numero é o maximo onde ele vai, o terceiro numero
# é o intervalo de quanto em quanto ele vai. A função range pede 3 parametros, 1 valor inicial,
# 2 até onde vai somando + 1 e o ultimo numero é de quanto em quanto
numero_tabuada = int(input("Escreva um numero: "))


for contador in range(1, 11, 1):
   resultado = numero_tabuada * contador
   print(f"{numero_tabuada} X {contador} = {resultado}")