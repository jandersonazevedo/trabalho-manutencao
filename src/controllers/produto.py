from ..models.produtos import Produto
from classes_DB_loja import ConexaoDb

class ProdutoController:
    @classmethod
    def CadastraProduto(produto: Produto):
        (nome, qtd_disponivel, tipo, data_chegada, descricao, preco) = produto
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("INSERT INTO produtos (nome_produto, qtd_disponivel, tipo, data_chegada, descricao) VALUES (%s, %s, %s, %s, %s, %s);",
                       (nome, qtd_disponivel, tipo, data_chegada, descricao, preco))
        ConexaoDb.conn.commit()
        print("Produto {nome} cadastrado com sucesso.")
    
    @classmethod
    def EditaProduto(produto: Produto):
        (id_produto, nome, qtd_disponivel, tipo, data_chegada, descricao, preco) = produto
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("UPDATE produtos SET nome_produto = %s, qtd_disponivel = %s, tipo = %s, data_chegada = %s, descricao = %s, preco = %s WHERE id_produto = %s;",
                       (nome, qtd_disponivel, tipo, data_chegada, descricao, id_produto, preco))
        ConexaoDb.conn.commit()
        print("Produto alterado para {nome} com sucesso.")

    @classmethod
    def ExcluiProduto(produto: Produto):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id_produto = %s;", (produto.id_produto))
        ConexaoDb.conn.commit()
        print("Produto excluído com sucesso.")