vendedor = ["João", "Paulo", "Sérgio", "Ana", "Maria", "Pedro"]
vendas = [1000, 1200, 900, 1300, 2000, 1700]

listaTuplas = zip(vendedor, vendas)

dicVendas = dict(listaTuplas)
print(dicVendas)