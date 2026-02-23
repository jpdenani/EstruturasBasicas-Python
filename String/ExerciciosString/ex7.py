texto = input("Digite um texto: ")

if texto:
    texto = texto.strip()
    vogais = (texto.count("a") + 
              texto.count("e") + 
              texto.count("i") + 
              texto.count("o") +
              texto.count("u"))
    texto = texto.replace(" ","")
    consoantes = len(texto) - vogais

    print(f"O texto tem {vogais} vogais")
    print(f"O texto tem {consoantes} consoantes")
else:
    print("Digite um texto")    
