meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
vendas_1sem = [25000, 29000, 22200, 17750, 15870, 19900]
vendas_2sem = [19850, 20120, 17540, 15555, 49051, 9650]

vendas_1sem.extend(vendas_2sem)

maiorVenda = max(vendas_1sem)
i = vendas_1sem.index(maiorVenda)

menorVenda = min(vendas_1sem)
p = vendas_1sem.index(menorVenda)

print(f"O mês de maior venda foi {meses[i]}, com {maiorVenda} vendas e o mês de menor venda foi {meses[p]}, com {menorVenda} vendas")

faturamento = sum(vendas_1sem)
percMaior = (maiorVenda/faturamento)*100
print(f"O faturamento foi de {faturamento} e o melhor mês representou {percMaior}%")