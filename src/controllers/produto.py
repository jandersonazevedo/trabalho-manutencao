from ...db import ConexaoDb

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from models.produto import Produto

class ProdutoController:
    @classmethod
    def CadastraProduto(cls, produto: Produto):
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
    def EditaProduto(cls, produto: Produto):
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
    def ExcluiProduto(cls, produto: Produto):
        id_produto = produto.id_produto
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id_produto = %s;", (id_produto,))
        ConexaoDb.conn.commit()
        print("Produto excluído com sucesso.")
