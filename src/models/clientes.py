from classes_DB_loja import ConexaoDb

class Cliente:
    def __init__(self, id_cliente, nome_cliente, cpf, contato, endereco):
        self.id_cliente = id_cliente
        self.nome_cliente = nome_cliente
        self.cpf = cpf
        self.contato = contato
        self.endereco = endereco

    def CadastraCliente(nome, cpf, contato, endereco):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("INSERT INTO clientes (nome_cliente, cpf, contato, endereco) VALUES (%s, %s, %s, %s);",
                       (nome, cpf, contato, endereco))
        ConexaoDb.conn.commit()
        print("Cliente {nome} cadastrado com sucesso.")

    def EditaCliente(id_cliente, nome, cpf, contato, endereco):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("UPDATE clientes SET nome_cliente = %s, cpf = %s, contato = %s, endereco = %s WHERE id_cliente = %s;",
                       (nome, cpf, contato, endereco, id_cliente))
        ConexaoDb.conn.commit()
        print("Cliente alterado para {nome} com sucesso.")

    def ExcluiCliente(id_cliente):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id_cliente = %s;", (id_cliente,))
        ConexaoDb.conn.commit()
        print("Cliente excluído com sucesso.")