produtos = []
produto = input("Digite um produto. Para sair, apenas aperte ENTER: ")

while produto:
    produtos.append(produto)
    produto = input("Digite um produto. Para sair, apenas aperte ENTER: ")

print(f"Registro finalizado, produtos cadastrados: {produtos}")
