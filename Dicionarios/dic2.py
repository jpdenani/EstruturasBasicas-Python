maisVendas = {"tecnologia" : "iphone", "cozinha":"frigideira","livros":"MAUS", "eletrodomestico":"geladeira"}
vendasTec = {"iphone":1000, "televisao":700,"smartwatch":750}

vendasTec["computador"] = 2000

print(vendasTec)

vendasTec["televisao"] = 800

print(vendasTec["televisao"])

del vendasTec["smartwatch"]

print(vendasTec)

IX = vendasTec.pop("iphone")
print(IX)
print(vendasTec)

vendasTec.clear()

print(vendasTec)