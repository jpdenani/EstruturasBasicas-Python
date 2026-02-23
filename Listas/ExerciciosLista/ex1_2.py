produtos = ['computador', 'livro', 'tablet', 'celular', 'tv', 'ar condicionado', 'alexa', 'máquina de café', 'kindle']

produtos_ecommerce = [
    [10000, 2500],
    [50000, 40],
    [7000, 1200],
    [20000, 1500],
    [5800, 1300],
    [7200, 2500],
    [200, 800],
    [3300, 700],
    [1900, 400]
]

if "livro" in produtos:
    iLivro = produtos.index("livro")
    totalAntigo = produtos_ecommerce[iLivro][0]*produtos_ecommerce[iLivro][1]
    produtos_ecommerce[iLivro][1] = produtos_ecommerce[iLivro][1]*1.1
    totalNovo = produtos_ecommerce[iLivro][0]*produtos_ecommerce[iLivro][1]
    print(f"Pagaremos R${totalNovo-totalAntigo} de imposto a mais")
else:
    print("Não vendemos livros")