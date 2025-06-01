from dados import livros

def buscar_por_titulo(titulo_busca):
    for livro in livros:
        if livro['titulo'].lower() == titulo_busca.lower():
            return livro
    return None
#