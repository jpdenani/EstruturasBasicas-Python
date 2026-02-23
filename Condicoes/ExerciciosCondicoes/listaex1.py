num1 = (input("Insira o primeiro número: "))
num2 = (input("Insira o segundo número: "))

if num1 and num2:
    num1 = int(num1)
    num2 = int(num2)
    if num1 > num2:
        print("O primeiro número é maior")
    elif num1 == num2:
        print ("Os números são iguais")
    else:
        print("O segundo número é maior")
else:
    print("Preencha as informações pedidas corretamente")            