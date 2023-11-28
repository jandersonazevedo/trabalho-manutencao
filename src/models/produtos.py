from classes_DB_loja import ConexaoDb

class Produto:
    def __init__(self, id_produto, nome_produto, qtd_disponivel, tipo, data_chegada, descricao, preco):
        self.id_produto = id_produto
        self.nome_produto = nome_produto
        self.qtd_disponivel = qtd_disponivel
        self.tipo = tipo
        self.data_chegada = data_chegada
        self.descricao = descricao
        self.preco = preco
