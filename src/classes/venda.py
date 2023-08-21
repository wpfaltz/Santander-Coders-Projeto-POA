class Venda:
    """
    Necessita do cliente, os produtos vendidos, valor total da venda e data e hora da venda.

    Data no formato dd/mm/yyyy
    Horario no formato HH:MM

    Atributos:
    data: str
    hora: str
    produtos: str
    cliente: str
    valor_total: float


    """
    def __init__(self, data, hora, produtos, cliente, valor_total):
        self.data = data
        self.hora = hora
        self.produtos = produtos
        self.cliente = cliente
        self.valor_total = valor_total