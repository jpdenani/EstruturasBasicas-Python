cpf = input("Digite seu CPF: ")

cpf = cpf.replace(".","")
cpf = cpf.replace("-","")
tam = len(cpf)

if cpf and tam == 11 and cpf.isnumeric():
    print(f"CPF: {cpf}")
else:
    print("Insira um cpf válido")    