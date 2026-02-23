vendedores = ["Carlos", "Maria", "João", "Roberto","Jonas","Pedro"]
vendas = [100,90,80,65,60,55]

meta = 70
i = 0

while vendas[i] > meta:
    print(f"{vendedores[i]} bateu a meta")
    i += 1
   