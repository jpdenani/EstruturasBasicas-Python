vendedor = ["João", "Paulo", "Sérgio", "Ana", "Maria", "Pedro"]
vendas = [1000, 1200, 900, 1300, 2000, 1700]

maxVenda = max(vendas)
i = vendas.index(maxVenda)

minVenda = min(vendas)
p = vendas.index(minVenda)

print(f"O melhor vendedor foi {vendedor[i]}, com {maxVenda} vendas.")
print(f"O pior vendedor foi {vendedor[p]}, com {minVenda} vendas.")

vendas.sort()
print(vendas)

vendas.sort(reverse=True)
print(vendas)