minBebida = 75
minAlimento = 50
minLimpeza = 30

nome = input("Informe o nome do produto: ")
categoria = input("Informe a categoria do produto: ")
qtdEstoque = int(input("Informe a quantidade em estoque: "))

if nome == "" or categoria == "" or qtdEstoque == "":
    print("Preencha as informações corretamente.")
else:
    if categoria == "Bebida":
        if qtdEstoque < minBebida:
            print(f"Solicitar compra de {nome} para a equipe de compras, {minBebida - qtdEstoque} unidades abaixo do mínimo")
    elif categoria == "Alimento":
        if qtdEstoque < minAlimento:
            print(f"Solicitar compra de {nome} para a equipe de compras, {minAlimento - qtdEstoque} unidades abaixo do mínimo")
    elif categoria == "Limpeza":
        if qtdEstoque < minLimpeza:
            print(f"Solicitar compra de {nome} para a equipe de compras, {minAlimento - qtdEstoque} unidades abaixo do mínimo")
     
         
