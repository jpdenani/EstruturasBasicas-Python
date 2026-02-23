vendas = [1000,2000,3000,1500,2500,1700,1750,1450,1350,400,1010,1000,2010,1030,1100]
meta = 1200
perc = 0
for venda in vendas:
    if venda >= 1200:
        print(f"Meta batida, {venda} vendas")
        perc += 1
    else:
        print("Não bateu a meta")
    percBatido = (perc/len(vendas))*100
else:
    print(f"{percBatido}% dos vendedores bateram a meta")    
            