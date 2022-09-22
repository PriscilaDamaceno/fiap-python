faturamento_anual = 0
maior_faturamento = 0
menor_faturamento = 0
for mes in range(1, 13, 1):
    faturamento_mes = float(input(f"Informe o faturamento do mês {mes}:  "))
    faturamento_anual = faturamento_anual + faturamento_mes

if mes == 1:
    faturamento_mes > maior_faturamento
    maior_faturamento = faturamento_mes
if faturamento_mes < menor_faturamento:
   menor_faturamento = faturamento_mes

faturamento_medio = faturamento_anual /12
print(f"A media de faturamento foi de R${faturamento_medio:.2f}")

