class Laboratorio:
    """
    Necessita do nome do laboratorio, endereco, telefone, cidade e estado em que se localiza.

    Atributos:
    nome: str
    endereco: str
    telefone: str
    cidade: str
    estado: str

    """
    def __init__(self, nome, endereco, telefone, cidade, estado):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.cidade = cidade
        self.estado = estado