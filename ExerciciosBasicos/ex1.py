venCoca = 150
venPepsi = 130
precoCoca = 1.50
precoPepsi = 1.50
custoLoja = 2500

fatPepsi = venPepsi*precoPepsi
fatCoca = venCoca*precoCoca
lucro = (fatPepsi + fatCoca) - custoLoja
margem = lucro/(fatCoca + fatPepsi) 

print("O faturamento com coca foi de: " + str(fatCoca)) #str transforma o tipo da variável para poder ser concatenada com o texto
print("O faturamento com pepsi foi de: {}".format(fatPepsi)) #{} e .format formatam as variáveis automaticamente
print(f"O faturamento total foi de: {fatCoca+fatPepsi}") #f-string (f antes da string) também é uma opção para essa formatação
print("O lucro total foi de: {}. E a margem foi de: {}".format(lucro,margem))

bebida = input("Qual o código da bebida?")
print("BAC" in bebida)
