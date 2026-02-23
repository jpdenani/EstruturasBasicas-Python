telefone = input("Digite o número de telefone: ")

if telefone:
    telefone = telefone.strip()
    telefone = telefone.replace("-","")
    if telefone.isnumeric():
        if len(telefone) <= 7:
            telefone = telefone + "3"
            print(f"Telefone: {telefone}")
        else:   
            print(f"Telefone: {telefone}") 
    else:
        print("Digite seu telefone corretamente")        
else:
    print("Digite seu número de telefone corretamente")        