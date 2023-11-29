from ...db import ConexaoDb

import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

from models.fornecedore import Fornecedor

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
    def ListarFornecedor(cls):
        cursor = ConexaoDb.conn.cursor()
        cursor.execute("SELECT * FROM fornecedor;")
        ConexaoDb.conn.commit()
