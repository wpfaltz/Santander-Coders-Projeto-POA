class MedicamentoQuimioterapico:
    """
    Necessita de nome do medicamento, principal composto do medicamento, laboratorio, descricao do medicamento e se ele necessita de receita.
    
    Atributos:
    nome: str
    principal_composto: str
    laboratorio: str
    descricao: str
    necessita_receita: bool
    """
    def __init__(self, nome, principal_composto, laboratorio, descricao, necessita_receita):
        self.nome = nome
        self.principal_composto = principal_composto
        self.laboratorio = laboratorio
        self.descricao = descricao
        self.necessita_receita = necessita_receita