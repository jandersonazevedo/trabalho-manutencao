import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from db.classes_DB_loja import ConexaoDb
from models.produto import Produto

class ProdutoController:
    @classmethod
    def cadastrar_produto(cls, produto: Produto):
        nome = produto.nome_produto
        qtd_disponivel = produto.qtd_disponivel
        tipo = produto.tipo
        data_chegada = produto.data_chegada
        descricao = produto.descricao
        preco = produto.preco

        cursor = ConexaoDb.conn.cursor()
        cursor.execute("INSERT INTO produtos (nome_produto, qtd_disponivel, tipo, data_chegada, descricao, preco) VALUES (%s, %s, %s, %s, %s, %s);",
                       (nome, qtd_disponivel, tipo, data_chegada, descricao, preco))
        ConexaoDb.conn.commit()
        print(f"Produto {nome} cadastrado com sucesso.")

    @classmethod
    def editar_produto(cls, produto: Produto):
        id_produto = produto.id_produto
        nome = produto.nome_produto
        qtd_disponivel = produto.qtd_disponivel
        tipo = produto.tipo
        data_chegada = produto.data_chegada
        descricao = produto.descricao
        preco = produto.preco

        cursor = ConexaoDb.conn.cursor()
        cursor.execute("UPDATE produtos SET nome_produto = %s, qtd_disponivel = %s, tipo = %s, data_chegada = %s, descricao = %s, preco = %s WHERE id_produto = %s;",
                       (nome, qtd_disponivel, tipo, data_chegada, descricao, preco, id_produto))
        ConexaoDb.conn.commit()
        print(f"Produto alterado para {nome} com sucesso.")

    @classmethod
    def excluir_produto(cls, produto: Produto):
        id_produto = produto.id_produto
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id_produto = %s;", (id_produto,))
        ConexaoDb.conn.commit()
        print("Produto excluído com sucesso.")

    @classmethod
    def listar_produtos(cls):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("SELECT * FROM produtos;")
        ConexaoDb.conn.commit()
