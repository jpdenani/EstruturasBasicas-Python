num = input("Digite um número")

if num:
    num = int(num)
    if num > 0:
        print("O número é positivo")
    elif num < 0:
        print("O número é negativo")
    else:
        print("0 é neutro")    
else:
    print("Digite o que foi solicitado")    