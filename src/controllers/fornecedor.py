from ..models.fornecedores import Fornecedor
from classes_DB_loja import ConexaoDb

class FornecedorController:
    @classmethod
    def CadastraFornecedor(fornecedor: Fornecedor):
        (nome, contato, produtos) = fornecedor
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("INSERT INTO fornecedor (nome_fornecedor, contato_fornecedor, produtos_fornecidos) VALUES (%s, %s, %s);",
                       (nome, contato, produtos))
        ConexaoDb.conn.commit()
        print("Fornecedor {nome} cadastrado com sucesso.")
    
    @classmethod
    def EditaFornecedor(fornecedor: Fornecedor):
        (id_fornecedor, nome, contato, produtos) = fornecedor
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("UPDATE fornecedor SET nome_fornecedor = %s, contato_fornecedor = %s, produtos_fornecidos = %s WHERE id_fornecedor = %s;",
                       (nome, contato, produtos, id_fornecedor))
        ConexaoDb.conn.commit()
        print("Fornecedor alterado para {nome} com sucesso.")
    
    @classmethod
    def ExcluiFornecedor(fornecedor: Fornecedor):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = %s;", (fornecedor.id_fornecedor))
        ConexaoDb.conn.commit()
        print("Fornecedor excluído com sucesso.")