produtos = ["Celular","Televisão","Controle","Ventilador","Pilha","Carregador"]
estoque = ["10", "5","15","10","20","10"]

produtos.append("Caixa")
estoque.append("30")

produtos.remove("Controle")
estoque.remove("15")

i = produtos.index("Caixa")

print(produtos)
print(estoque)
print(f"Produto: {produtos[i]}. Estoque: {estoque[i]}")

try:
    produtos.remove("Notebook")
    print(produtos)
except:
    print("Notebook não existe na lista")    