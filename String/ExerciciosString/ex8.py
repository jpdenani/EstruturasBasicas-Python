senha = input("Digite sua senha:")
num = [1,2,3,4,5,6,7,8,9,0]

if senha:
    num = str(num)
    if len(senha) >= 8 and num in senha:
        print("Senha forte")
    else:
        print("Senha fraca")
else: 
    print("Informe a senha")            