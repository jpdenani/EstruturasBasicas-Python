metaLoja = 100000
metaVendedor = 20000
vendaLoja = 100000
vendaVendedor = 30000
notaVendedor = 9

if vendaLoja >= metaLoja and (vendaVendedor >= metaVendedor or notaVendedor >= 9):
    bonus = 0.03
    print(f"O vendedor receberá {vendaVendedor*bonus}")
else:
    print("O vendedor não receberá nada")    