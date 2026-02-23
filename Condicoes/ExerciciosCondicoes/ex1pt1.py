meta = 1000
vendasF1 = 1000
vendasF2 = 770
vendasF3 = 2700

if vendasF1 >= meta:
    bonus = 0.10
    print(f"O bônus do funcionário 1 foi de {bonus*vendasF1}")
else:
    print("O funcionário 1 não bateu a meta")

if vendasF2 >= meta:
    bonus = 0.10
    print(f"O bônus do funcionário 2 foi de {bonus*vendasF2}")
else:
    print("O funcionário 2 não bateu a meta")  

if vendasF3 >= meta:
    bonus = 0.10
    print(f"O bônus do funcionário 3 foi de {bonus*vendasF3}")
else:
    print("O funcionário 3 não bateu a meta")  