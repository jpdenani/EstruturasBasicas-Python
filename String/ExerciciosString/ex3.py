texto1 = input("Digite o primeiro texto: ")
texto2 = input("Digite o segundo texto: ")

tam1 = len(texto1)
tam2 = len(texto2)

if texto1 and texto2:
    print(f"Tamanho do texto 1: {tam1}")
    print(f"Tamanho do texto 2: {tam2}")
    if tam1 == tam2:
        print("Os textos são do mesmo tamanho")
    else:
        print("Os textos são de tamanhos diferentes")
    if texto1 == texto2:
        print("Os textos são iguais")
    else:     
        print("Os textos são diferentes")   
else:
    print("Informe os textos")                
