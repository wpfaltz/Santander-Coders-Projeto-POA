import json

class Cliente:
    """
    Necessita de CPF, nome e data de nascimento do cliente.

    Formato data_nascimento: yyyy-mm-dd
    """
    def __init__(self, cpf, nome, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

    @staticmethod
    def carregar_clientes():
        with open(r'src/db/clientes.json', "r") as file:
            return json.load(file)
    
    @staticmethod
    def salvar_clientes(clientes):
        with open(r'src/db/clientes.json', "w") as file:
            json.dump(clientes, file, indent=4)