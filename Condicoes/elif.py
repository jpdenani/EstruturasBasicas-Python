meta = 20000
venda = 19000

if venda > (meta*2):
    bonus = 0.07
    print(f"O bônus foi de {bonus*100}%")   
elif venda > meta:
    bonus = 0.03
    print(f"O bônus foi de {bonus*100}%") 
else:
    print("Não tem bônus :/")    