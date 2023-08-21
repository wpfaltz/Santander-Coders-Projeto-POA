from src.classes.cliente import Cliente
from src.classes.laboratorio import Laboratorio
from src.classes.medicamentofitoterapico import MedicamentoFitoterapico
from src.classes.medicamentoquimioterapico import MedicamentoQuimioterapico
from src.classes.venda import Venda
import os

def main():
    print("Selecione a opcao desejada:\n"
          "1-Cadastrar cliente\n"
          "2-Cadastrar medicamento\n"
          "3-Efetuar venda\n"
          "4-Sair")
    
    opcao = input("Insira a opção desejada: ")

    while opcao not in ['1', '2', '3', '4']:
        print("Opção inválida! Tente novamente.")
        opcao = input("Insira a opção desejada: ")

    if opcao == '1':
        os.system('cls')
        print("Opção selecionada: 1-Cadastrar cliente\n")
        cadastrar_cliente()
    
    elif opcao == '2':
        os.system('cls')
        print("Opção selecionada: 2-Cadastrar medicamento\n")

    elif opcao == '3':
        os.system('cls')
        print("Opção selecionada: 3-Efetuar venda\n")

    elif opcao == '4':
        os.system('cls')
        print("Opção selecionada: 4-Sair")

def cadastrar_cliente():
    cpf = input("Digite o CPF do cliente: ")
    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente no formato yyyy-mm-dd: ")
    novo_cliente = Cliente(cpf, nome, data_nascimento)

    # Carregar os clientes existentes
    clientes = Cliente.carregar_clientes()

    # Adicionar o novo cliente à lista
    clientes.append(novo_cliente)

    # Salvar a lista atualizada de clientes
    Cliente.salvar_clientes(clientes)

    print("Cliente cadastrado com sucesso!")

if __name__ == "__main__":
    main()