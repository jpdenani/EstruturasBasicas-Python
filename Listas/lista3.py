produtos = ["Celular","Televisão","Controle","Ventilador","Pilha","Carregador"]
estoque = [11, 5, 15, 12, 20, 13]

tam = len(produtos)
maiorEstoque = max(estoque)
menorEstoque = min(estoque)

imr = estoque.index(maiorEstoque)
imn = estoque.index(menorEstoque)

print(produtos[imr])
print(produtos[imn])
