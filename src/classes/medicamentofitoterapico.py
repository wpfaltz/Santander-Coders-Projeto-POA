class MedicamentoFitoterapico:
    """
    Necessita de nome do medicamento, principal composto do medicamento, laboratorio, descricao do medicamento.
    
    Atributos:
    nome: str
    principal_composto: str
    laboratorio: str
    descricao: str
    """
    def __init__(self, nome, principal_composto, laboratorio, descricao):
        self.nome = nome
        self.principal_composto = principal_composto
        self.laboratorio = laboratorio
        self.descricao = descricao