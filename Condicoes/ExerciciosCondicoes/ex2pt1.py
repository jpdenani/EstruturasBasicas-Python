
vendasF1 = 2000
vendasF2 = 1000
vendasF3 = 500

if vendasF1 >= 2000:
    bonus = 0.15
    print(f"O bônus do funcionário 1 foi de {bonus*vendasF1}")
elif vendasF1 >= 1000:
    bonus = 0.10
    print(f"O bônus do funcionário 1 foi de {bonus*vendasF1}")
else:
    print("O funcionário 1 não bateu a meta")

if vendasF2 >= 2000:
    bonus = 0.15
    print(f"O bônus do funcionário 2 foi de {bonus*vendasF2}")
elif vendasF2 >= 1000:
    bonus = 0.10
    print(f"O bônus do funcionário 2 foi de {bonus*vendasF2}")
else:
    print("O funcionário 2 não bateu a meta")  

if vendasF3 >= 2000:
    bonus = 0.15
    print(f"O bônus do funcionário 3 foi de {bonus*vendasF3}")
elif vendasF3 >= 1000:
    bonus = 0.10
    print(f"O bônus do funcionário 3 foi de {bonus*vendasF3}")
else:
    print("O funcionário 3 não bateu a meta")  