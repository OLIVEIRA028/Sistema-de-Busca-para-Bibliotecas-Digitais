from catalogo import listar_livros, cadastrar_livro
from busca import buscar_por_titulo
from ordenacao import ordenar_por_titulo

def menu():
    while True:
        print("\n╔" + "═"*28 + "╗")
        print("║📚 Sistema de Biblioteca 📚 ║")
        print("╠" + "═"*28 + "╣")
        print("║ 1 - Listar livros          ║")
        print("║ 2 - Cadastrar livro        ║")
        print("║ 3 - Buscar por título      ║")
        print("║ 4 - Ordenar por título     ║")
        print("║ 0 - Sair                   ║")
        print("╚" + "═"*28 + "╝")

        opcao = input("\nEscolha uma opção: ")
        
        if opcao == "1":
            print("\n╔" + "═"*24 + "╗")
            print("║   📖 Lista de Livros   ║")
            print("╚" + "═"*24 + "╝")
            listar_livros()


        elif opcao == "2":
            print("\n╔" + "═"*26 + "╗")
            print("║   ✍️ Cadastro de Livro   ║")
            print("╚" + "═"*26 + "╝")
            cadastrar_livro()

        elif opcao == "3":
            titulo = input("Digite o título a buscar: ")
            resultado = buscar_por_titulo(titulo)
            print("\n╔" + "═"*28 + "╗")
            if resultado:
                print(f"║ Encontrado: {resultado['titulo']}   ║")
                print(f"║     {resultado['autor']} ({resultado['ano']})║")
            else:
                print("║      Livro não encontrado.    ║")
            print("╚" + "═"*28 + "╝")

        elif opcao == "4":
            print("\n╔" + "═"*28 + "╗")
            print("║     📚 Livros Ordenados     ║")
            print("╚" + "═"*28 + "╝")
            ordenar_por_titulo()

        elif opcao == "0":
            print("\n╔" + "═"*28 + "╗")
            print("║🚪 Encerrando o sistema...  ║")
            print("╚" + "═"*28 + "╝")
            break

        else:
            print("\n╔" + "═"*20 + "╗")
            print("║❌ Opção inválida!  ║")
            print("╚" + "═"*20 + "╝")

menu()

#