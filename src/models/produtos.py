from classes_DB_loja import ConexaoDb

class Produto:
    def __init__(self, id_produto, nome_produto, qtd_disponivel, tipo, data_chegada, descricao):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.qtd_disponivel = qtd_disponivel
        self.tipo = tipo
        self.data_chegada = data_chegada
        self.descricao = descricao

    def CadastraProduto(nome, qtd_disponivel, tipo, data_chegada, descricao):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("INSERT INTO produtos (nome_produto, qtd_disponivel, tipo, data_chegada, descricao) VALUES (%s, %s, %s, %s, %s);",
                       (nome, qtd_disponivel, tipo, data_chegada, descricao))
        ConexaoDb.conn.commit()
        print(f"Produto {nome} cadastrado com sucesso.")

    def EditaProduto(id_produto, nome, qtd_disponivel, tipo, data_chegada, descricao):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("UPDATE produtos SET nome_produto = %s, qtd_disponivel = %s, tipo = %s, data_chegada = %s, descricao = %s WHERE id_produto = %s;",
                       (nome, qtd_disponivel, tipo, data_chegada, descricao, id_produto))
        ConexaoDb.conn.commit()
        print(f"Produto alterado para {nome} com sucesso.")

    def ExcluiProduto(id_produto):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("DELETE FROM produtos WHERE id_produto = %s;", (id_produto,))
        ConexaoDb.conn.commit()
        print("Produto excluído com sucesso.")