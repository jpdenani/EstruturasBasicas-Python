maisVendas = {"tecnologia" : "iphone", "cozinha":"frigideira","livros":"MAUS", "eletrodomestico":"geladeira"}
vendasTec = {"iphne":1000, "televisao":700,"smartwatch":750}

if "iphone" in vendasTec:
    qtdIphone = vendasTec["iphone"]
    print(qtdIphone)
else:
    print("Não tem iphone")    

livro = maisVendas["livros"]
eletrodomestico = maisVendas["eletrodomestico"]

print(livro)
print(eletrodomestico)

qtdTV = vendasTec["televisao"]
qtdSW = vendasTec["smartwatch"]

print(qtdTV)
print(qtdSW)