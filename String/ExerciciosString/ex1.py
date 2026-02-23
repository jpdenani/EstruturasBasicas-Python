cpf = input("Digite seu CPF (apenas com números): ")

cpf = cpf.strip() 
cpf = cpf.replace(".","") 
cpf = cpf.replace("-","") 

if cpf.isnumeric() and len(cpf) == 11:
    print(f"OK. CPF: {cpf}")
else:
    print("Digite seu CPF corretamente e apenas com números")     