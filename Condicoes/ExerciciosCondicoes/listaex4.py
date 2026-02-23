orc1 = input("Digite o primeiro orçamento: ")
orc2 = input("Digite o segundo orçamento: ")
orc3 = input("Digite o terceiro orçamento: ")

if orc1 and orc2 and orc3:
    orc1 = int(orc1)
    orc2 = int(orc2)
    orc3 = int(orc3)
    if orc1 > orc3 and orc2 > orc3:
        print("O terceiro orçamento é o menor")
    elif orc3 > orc1 and orc2 > orc1:
        print("O primeiro orçamento é o menor")
    else:
        print("O segundo orçamento é o menor")
else:
    print("Digite as informações corretamente")