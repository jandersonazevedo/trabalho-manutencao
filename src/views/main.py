from models import Produto, Fornecedor, Cliente
from ...db.classes_DB_loja import ConexaoDb

class Menu:
    @classmethod
    def exibir_menu(cls):
        while True:
            print("\n------ Menu Principal ------")
            print("1. Gerenciar Produtos")
            print("2. Gerenciar Fornecedores")
            print("3. Gerenciar Clientes")
            print("0. Sair")

            escolha = input("Digite o número da opção desejada: ")

            if escolha == "1":
                cls.cadastrar_produto()
            elif escolha == "2":
                cls.menu_fornecedores()
            elif escolha == "3":
                cls.menu_clientes()
            elif escolha == "0":
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

    @classmethod
    def menu_produtos(cls):
        while True:
            print("\n------ Menu de Produtos ------")
            print("1. Cadastrar Produto")
            print("2. Editar Produto")
            print("3. Excluir Produto")
            print("0. Voltar ao Menu Principal")

            escolha = input("Digite o número da opção desejada: ")

            if escolha == "1":
                cls.cadastrar_produto()
            elif escolha == "2":
                cls.editar_produto()
            elif escolha == "3":
                cls.excluir_produto()
            elif escolha == "0":
                break
            else:
                print("Opção inválida. Tente novamente.")

    @classmethod
    def menu_fornecedores(cls):
        # Implemente de maneira semelhante ao menu_produtos
        pass

    @classmethod
    def menu_clientes(cls):
        # Implemente de maneira semelhante ao menu_produtos
        pass

    @classmethod
    def cadastrar_produto(cls):
        # Implemente
        pass

if __name__ == "__main__":
    Menu.exibir_menu()