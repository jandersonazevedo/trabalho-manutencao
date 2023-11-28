from ..models.fornecedores import Fornecedor
from classes_DB_loja import ConexaoDb

class FornecedorController:
    @classmethod
    def CadastraFornecedor(cls, fornecedor: Fornecedor):
        nome = fornecedor.nome_fornecedor
        contato = fornecedor.contato_fornecedor
        produtos = fornecedor.produtos_fornecidos

        cursor = ConexaoDb.conn.cursor()
        cursor.execute("INSERT INTO fornecedor (nome_fornecedor, contato_fornecedor, produtos_fornecidos) VALUES (%s, %s, %s);",
                       (nome, contato, produtos))
        ConexaoDb.conn.commit()
        print(f"Fornecedor {nome} cadastrado com sucesso.")

    @classmethod
    def EditaFornecedor(cls, fornecedor: Fornecedor):
        id_fornecedor = fornecedor.id_fornecedor
        nome = fornecedor.nome_fornecedor
        contato = fornecedor.contato_fornecedor
        produtos = fornecedor.produtos_fornecidos

        cursor = ConexaoDb.conn.cursor()
        cursor.execute("UPDATE fornecedor SET nome_fornecedor = %s, contato_fornecedor = %s, produtos_fornecidos = %s WHERE id_fornecedor = %s;",
                       (nome, contato, produtos, id_fornecedor))
        ConexaoDb.conn.commit()
        print(f"Fornecedor alterado para {nome} com sucesso.")

    @classmethod
    def ExcluiFornecedor(cls, fornecedor: Fornecedor):
        id_fornecedor = fornecedor.id_fornecedor
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = %s;", (id_fornecedor,))
        ConexaoDb.conn.commit()
        print("Fornecedor excluído com sucesso.")
