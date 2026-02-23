email = input("Digite seu email: ")

if email:
    pos = email.find("@")
    if email[0] != "@" and email[-1] != "@" and pos != -1 and "." in email[pos:]:
        print("Email válido")
    else:
        print("Email inválido")
else:
    print("Informe o email")    