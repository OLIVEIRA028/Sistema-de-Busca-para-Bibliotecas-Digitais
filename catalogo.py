from dados import livros

def listar_livros():
    if not livros:
        print("\nNenhum livro cadastrado.")
        return
    for i, livro in enumerate(livros, 1):
        print(f"{i}. {livro['titulo']} - {livro['autor']} ({livro['ano']})")

def cadastrar_livro():
    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    livros.append({"titulo": titulo, "autor": autor, "ano": ano})
    print("Livro cadastrado com sucesso!")
