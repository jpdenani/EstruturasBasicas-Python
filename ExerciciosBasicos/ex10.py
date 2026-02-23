tam = float(input("Insira o tamanho do arquivo em MB: "))
vel = float(input("Insira a velocidade da internet em Mbps: "))
tempo = (tam*8/vel)/60
print(f"O tempo em minutos para download é: {tempo}")