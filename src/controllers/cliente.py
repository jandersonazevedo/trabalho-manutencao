from ..models.clientes import Cliente
from classes_DB_loja import ConexaoDb

class ClienteController:
    @classmethod
    def CadastraCliente(cls, cliente: Cliente):
        nome = cliente.nome_cliente
        cpf = cliente.cpf
        contato = cliente.contato
        endereco = cliente.endereco

        cursor = ConexaoDb.conn.cursor()
        cursor.execute("INSERT INTO clientes (nome_cliente, cpf, contato, endereco) VALUES (%s, %s, %s, %s);",
                       (nome, cpf, contato, endereco))
        ConexaoDb.conn.commit()
        print(f"Cliente {nome} cadastrado com sucesso.")

    @classmethod
    def EditaCliente(cls, cliente: Cliente):
        id_cliente = cliente.id_cliente
        nome = cliente.nome_cliente
        cpf = cliente.cpf
        contato = cliente.contato
        endereco = cliente.endereco

        cursor = ConexaoDb.conn.cursor()
        cursor.execute("UPDATE clientes SET nome_cliente = %s, cpf = %s, contato = %s, endereco = %s WHERE id_cliente = %s;",
                       (nome, cpf, contato, endereco, id_cliente))
        ConexaoDb.conn.commit()
        print(f"Cliente alterado para {nome} com sucesso.")

    @classmethod
    def ExcluiCliente(cls, cliente: Cliente):
        id_cliente = cliente.id_cliente
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id_cliente = %s;", (id_cliente,))
        ConexaoDb.conn.commit()
        print("Cliente excluído com sucesso.")

