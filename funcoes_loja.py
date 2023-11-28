import classes_DB_loja
import os

# Menu principal do sistema
def MenuPrincipal():
    opcao = 0
    try:
        while (opcao != 5):
            # limpa tela
            os.system("cls" if os.name == "nt" else "clear")
            print(" "*25,"+ ".ljust(45,"-"),"+")
            print(" "*25,"|      SEJA BEM VINDO AO SISTEMA DA LOJA      |")
            print(" "*25,"+ ".ljust(45,"-"),"+")
            print(" ")
            print("Menu Principal:")
            print("="*58)
            print("| 1 - Cadastrar Produto    |  2 - Alterar Produto        |")
            print("| 3 - Excluir Produto      |  4 - Visualizar Produtos    |")
            print("| 5 - Adicionar fornecedor |  6 - Alterar fornecedor     |")
            print("| 7 - Excluir fornecedor   |  8 - Visualizar fornecedores|")
            print("|                     9 - Encerrar                       |")
            print("="*58)
            opcao = int(input("Digite a opção desejada: "))
            # limpa tela
            os.system("cls" if os.name == "nt" else "clear")
            if (opcao == 1):
                produto = input("Qual produto deseja cadastrar: ")
                try:    
                    classes_DB_loja.db.MenuCadastrar(produto)
                    input("Pressione enter para continuar...")
                except:
                    print('Erro ao cadastrar, produto já existe..')
                    input("Pressione enter para continuar...")
            elif (opcao == 2):
                id = input("Digite o ID do produto que vai ser alterado: ")
                produto = input("Digite o nome do produto que vai ser alterado: ")
                classes_DB_loja.db.MenuAlterar(produto,id)
                input("Pressione enter para continuar...")
            elif (opcao == 3):
                id = input("Digite o ID do produto que será excluido: ")
                classes_DB_loja.db.MenuExluir(id)
                input("Pressione enter para continuar...")
            elif (opcao == 4):
                classes_DB_loja.db.MenuVisualizar()
                input("Pressione enter para continuar...")
            elif (opcao == 5):
                novo_fornecedor = classes_DB_loja.Fornecedor()
                fornecedor_nome = input("Digite o nome do fornecedor: ")
                fornecedor_contato = input("Digite o contato (com DDD) do fornecedor: ")
                fornecedor_produtos = input("Digite o(s) produto(s) fornecidos: ")
                novo_fornecedor.CadastraFornecedor(fornecedor_nome, fornecedor_contato, fornecedor_produtos)
                input("Pressione enter para continuar...")
            elif (opcao == 6):
                fornecedor_id = input("Digite o ID do fornecedor a ser alterado: ")
                fornecedor_nome = input("Digite o novo nome do fornecedor(caso deseje alterar): ")
                fornecedor_contato = input("Digite o(s) nome(s) do(s) produto(s) a serem alterados: ")
                fornecedor_produtos = input("Digite o(s) produto(s) a serem alterados: ")
                fornecedor = classes_DB_loja.Fornecedor()
                fornecedor.EditaFornecedor(fornecedor_id, fornecedor_nome, fornecedor_contato, fornecedor_produtos)
                input("Pressione enter para continuar...")
            elif (opcao == 7):
                fornecedor_id = input("Digite o ID do fornecedor que deseja excluir: ")
                fornecedor = classes_DB_loja.Fornecedor()
                fornecedor.ExcluiFornecedor(fornecedor_id)
                input("Pressione enter para continuar...")

            elif (opcao == 8):
                fornecedor = classes_DB_loja.Fornecedor()
                fornecedor.VisualizarFornecedores()
                input("Pressione enter para continuar...")

            elif (opcao == 9):
                print("Sistema encerrado pelo usuário...")
                break
            else:
                print("Opção inválida...")
                input("Pressione enter para continuar...")
    except:
        print("Opção inválida...")
        input("Pressione enter para continuar...")
        MenuPrincipal()
        