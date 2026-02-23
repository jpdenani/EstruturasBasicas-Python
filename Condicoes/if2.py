rendimento = 0.21

if rendimento > 0.05:
    if rendimento > 0.20:
        taxa = 0.04
        print(f"A taxa foi de {taxa*100}%")
    else:
        taxa = 0.02
        print(f"A taxa foi de {taxa*100}%")     
else:
    taxa = 0.0
    print(f"A taxa foi de {taxa}%")           