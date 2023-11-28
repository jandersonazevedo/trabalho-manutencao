from ..models.clientes import Cliente
from classes_DB_loja import ConexaoDb


class ClienteController:
    @classmethod
    def CadastraCliente(cleinte: Cliente):
        (nome, cpf, contato, endereco) = cleinte
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("INSERT INTO clientes (nome_cliente, cpf, contato, endereco) VALUES (%s, %s, %s, %s);",
                       (nome, cpf, contato, endereco))
        ConexaoDb.conn.commit()
        print("Cliente {nome} cadastrado com sucesso.")

    @classmethod
    def EditaCliente(cleinte: Cliente):
        (id_cliente, nome, cpf, contato, endereco) = cleinte
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("UPDATE clientes SET nome_cliente = %s, cpf = %s, contato = %s, endereco = %s WHERE id_cliente = %s;",
                       (nome, cpf, contato, endereco, id_cliente))
        ConexaoDb.conn.commit()
        print("Cliente alterado para {nome} com sucesso.")

    @classmethod
    def ExcluiCliente(cliente: Cliente):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id_cliente = %s;", (cliente.id_cliente))
        ConexaoDb.conn.commit()
        print("Cliente excluído com sucesso.")