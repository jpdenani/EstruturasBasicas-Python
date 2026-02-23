estoque = [
    [1000,2000,2500,400,800],
    [1100,2500,500,470,850],
    [750,800,1700,1200,2750],
    [1300,1235,1450,1250,3000],
    [1800,1000,3070,770,640]
]
fabricas = ["Fabrica A", "Fabrica B", "Fabrica C", "Fabrica D", "Fabrica E"]
nivelMin = 1000
fabricasAbaixoNivel = []

for i, lista in enumerate(estoque):
    for qtde in lista:
        if qtde < nivelMin:
            if fabricas[i] in fabricasAbaixoNivel:
                pass
            else:
                fabricasAbaixoNivel.append(fabricas[i])
print(fabricasAbaixoNivel)               
            