vendedores = ["João", "Pedro", "Paulo", "Carlos"]
produtos = ["celular", "tablet", "notebook"]
vendas = [[10, 20, 30],
          [15, 25, 35],
           [17, 27, 37],
            [19, 29, 39] ]

vendasJoaoCelular = vendas[0][0]
print(vendasJoaoCelular)

vendasPedroNotebook = vendas[1][2]
print(vendasPedroNotebook)

vendasPauloTablet = vendas[2][1]
print(vendasPauloTablet)

vendas[3][2] = 40
print(vendas)