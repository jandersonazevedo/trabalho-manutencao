from classes_DB_loja import ConexaoDb

class Fornecedor:
    def __init__(self, id_fornecedor, nome_fornecedor, contato_fornecedor, produtos_fornecidos):
        self.id_fornecedor = id_fornecedor
        self.nome_fornecedor = nome_fornecedor
        self.contato_fornecedor = contato_fornecedor
        self.produtos_fornecidos = produtos_fornecidos

    def CadastraFornecedor(nome, contato, produtos):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("INSERT INTO fornecedor (nome_fornecedor, contato_fornecedor, produtos_fornecidos) VALUES (%s, %s, %s);",
                       (nome, contato, produtos))
        ConexaoDb.conn.commit()
        print(f"Fornecedor {nome} cadastrado com sucesso.")

    def EditaFornecedor(id_fornecedor, nome, contato, produtos):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("UPDATE fornecedor SET nome_fornecedor = %s, contato_fornecedor = %s, produtos_fornecidos = %s WHERE id_fornecedor = %s;",
                       (nome, contato, produtos, id_fornecedor))
        ConexaoDb.conn.commit()
        print(f"Fornecedor alterado para {nome} com sucesso.")

    def ExcluiFornecedor(id_fornecedor):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("DELETE FROM fornecedor WHERE id_fornecedor = %s;", (id_fornecedor,))
        ConexaoDb.conn.commit()
        print("Fornecedor excluído com sucesso.")