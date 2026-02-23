vendas = []

while True:
    produto = input("Para sair pressione ENTER. Digite o produto: ")
    if not produto:
        break
    else:
        qtde = int(input("Digite a quantidade: "))
        vendas.append([produto, qtde])
        print(vendas)