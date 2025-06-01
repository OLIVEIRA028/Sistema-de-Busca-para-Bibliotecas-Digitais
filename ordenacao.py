from dados import livros

def quicksort(lista, chave):
    if len(lista) <= 1:
        return lista
    
    pivo = lista[0]
    menores = [x for x in lista[1:] if x[chave] < pivo[chave]]
    maiores = [x for x in lista[1:] if x[chave] >= pivo[chave]]
    
    return quicksort(menores, chave) + [pivo] + quicksort(maiores, chave)

def ordenar_por_titulo():
    ordenados = quicksort(livros, "titulo")
    for i, livro in enumerate(ordenados, 1):
        print(f"{i}. {livro['titulo']} - {livro['autor']} ({livro['ano']})")

#