produtos = ["Televisão", "Celular", "Computador", "Ventilador", "Teclado"]
precos = [2000,1500,4500,100,150]

for preco in precos:
    print(preco*1.15)

for i in range(len(precos)):
    produto = produtos[i]
    preco = precos[i]
    print(f"Produto: {produto}, Preço: {preco}")

for i, preco in enumerate(precos):
    produto = produtos[i]
    preco = preco*1.2
    print(f"Produto: {produto}, Preço: {preco}")