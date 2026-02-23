vendas = [
    ("20/02/2026", "iphone x", 1000, 2),
    ("21/02/2026", "iphone 11", 1500, 3),
    ("22/02/2026", "iphone 12", 1800, 1),
    ("23/02/2026", "iphone x", 1000, 1),
    ("24/02/2026", "iphone 13", 2100, 4)
]

fatIphoneX = 0

for venda in vendas:
    data, produto, valor, unidades = venda
    if produto == "iphone x":
        fatIphoneX += valor * unidades

print(fatIphoneX)  

prodMaisVendido = ""
qtdMaisVendido = 0

for venda in vendas:
    data, produto, valor, unidades = venda
    if unidades > qtdMaisVendido:
        prodMaisVendido = produto
        qtdMaisVendido = unidades
print(produto)        
