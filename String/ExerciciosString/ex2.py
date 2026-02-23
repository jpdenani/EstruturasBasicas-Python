nome = input("Digite seu primeiro nome: ")
email = input("Digite seu email: ")

if nome and email:
    nome = nome.strip()   
    pos1 = nome.find(" ")
    email = email.strip()

    if nome.isalpha():
        print(f"Nome: {nome}")
    else:
        print("Digite seu primeiro nome corretamente.")

    pos = email.find("@")
    if pos != -1 and "." in email[pos:]:
        print(f"Email: {email}")
    else:
        print("Digite seu email corretamente")    
else:
    print("Preencha os campos solicitados")          
    

