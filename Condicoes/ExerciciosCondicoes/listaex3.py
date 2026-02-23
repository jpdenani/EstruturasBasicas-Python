nota1 = input("Insira a primeira nota: ")
nota2 = input ("Insira a seguda nota: ")

if nota1 and nota2:
    nota1 = int(nota1)
    nota2 = int(nota2)
    media = (nota1 + nota2)/2
    if media == 10:
        print("Aprovado com distinção")
    elif media >= 7:
        print("Aprovado")
    else: 
        print("Reprovado")      
else:
    print("Insira as notas corretamente")          