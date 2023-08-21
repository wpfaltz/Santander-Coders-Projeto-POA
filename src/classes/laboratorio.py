import json

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

    @staticmethod
    def carregar_laboratorios():
        with open(r'src/db/laboratorios.json', "r") as file:
            return json.load(file)
    
    @staticmethod
    def salvar_laboratorios(laboratorios):
        with open(r'src/db/laboratorios.json', "w") as file:
            json.dump(laboratorios, file, indent=4)