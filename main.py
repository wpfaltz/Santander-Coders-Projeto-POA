from src.classes.cliente import Cliente
from src.classes.laboratorio import Laboratorio
from src.classes.medicamentofitoterapico import MedicamentoFitoterapico
from src.classes.medicamentoquimioterapico import MedicamentoQuimioterapico
from src.classes.venda import Venda
import os
import datetime

def main():
    print("Selecione a opcao desejada:\n"
          "1 - Cadastrar cliente\n"
          "2 - Cadastrar medicamento\n"
          "3 - Efetuar venda\n"
          "4 - Emitir relatórios\n"
          "5 - Sair")
    
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
        cadastrar_medicamento()

    elif opcao == '3':
        os.system('cls')
        print("Opção selecionada: 3-Efetuar venda\n")
    
    elif opcao == '4':
        os.system('cls')
        print("Opção selecionada: 4 - Emitir relatórios\n")

    elif opcao == '5':
        os.system('cls')
        print("Opção selecionada: 5-Sair")

def cadastrar_cliente():
    print("Cadastro de cliente:\n\n")
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

    main()

def cadastrar_medicamento():
    print("Qual é o tipo de medicamento que gostaria de adicionar?\n"
        "1-Medicamento fitoterápico\n"
        "2-Medicamento quimioterápico")
     
    opcao2 = input("Insira a opção desejada: ")

    while opcao2 not in ['1', '2']:
        print("Opção inválida! Tente novamente.")
        opcao2 = input("Insira a opção desejada: ")

    if opcao2 == '1':
        cadastrar_medicamento_fitoterapico()
    elif opcao2 == '2':
        cadastrar_medicamento_quimioterapico()

def cadastrar_medicamento_quimioterapico():
    nome = input("Digite o nome do medicamento: ")
    principal_composto = input("Digite o principal composto do medicamento: ")
    laboratorio = input("Digite o nome do laboratório: ")
    descricao = input("Digite a descrição do medicamento: ")
    necessita_receita = input("O medicamento necessita de receita? (S/N): ").upper()

    while necessita_receita not in ['S', 'N']:
        print("Opção inválida! Tente novamente")
        necessita_receita = input("O medicamento necessita de receita? (S/N): ").upper()

    novo_medicamento_quimioterapico = MedicamentoQuimioterapico(nome, principal_composto, laboratorio, descricao, necessita_receita)

    # Carregar os medicamentos quimioterápicos existentes
    todos_medicamentos_quimioterapicos = MedicamentoQuimioterapico.carregar_medicamentos()

    # Adicionar o novo medicamento à lista de todos os medicamentos quimioterápicos e à lista dos novos adicionados
    todos_medicamentos_quimioterapicos.append(novo_medicamento_quimioterapico.__dict__)
    medicamentos_quimio.append(novo_medicamento_quimioterapico)

    # Salvar a lista atualizada de medicamentos quimioterápicos
    MedicamentoQuimioterapico.salvar_medicamentos(todos_medicamentos_quimioterapicos)

    print("Medicamento quimioterápico cadastrado com sucesso!")

    main()

def cadastrar_medicamento_fitoterapico():
    nome = input("Digite o nome do medicamento: ")
    principal_composto = input("Digite o principal composto do medicamento: ")
    laboratorio = input("Digite o nome do laboratório: ")
    descricao = input("Digite a descrição do medicamento: ")

    novo_medicamento_fitoterapico = MedicamentoFitoterapico(nome, principal_composto, laboratorio, descricao)

    # Carregar os medicamentos fitoterápicos existentes
    todos_medicamentos_fitoterapicos = MedicamentoFitoterapico.carregar_medicamentos()

    # Adicionar o novo medicamento à lista de todos os medicamentos fitoterápicos e à lista dos novos adicionados
    todos_medicamentos_fitoterapicos.append(novo_medicamento_fitoterapico.__dict__)
    medicamentos_fito.append(novo_medicamento_fitoterapico)

    # Salvar a lista atualizada de medicamentos fitoterápicos
    MedicamentoFitoterapico.salvar_medicamentos(todos_medicamentos_fitoterapicos)

    print("Medicamento fitoterápico cadastrado com sucesso!")

    main()

def efetuar_venda():
    cliente_cpf = input("Digite o CPF do cliente: ")

    # Verificar se o cliente existe
    cliente = encontrar_cliente_por_cpf(cliente_cpf)

    if cliente is None:
        print("Cliente não encontrado.")
        cadastrar_agora = input("Deseja cadastrar um novo cliente agora? (S/N):").upper()

        while cadastrar_agora not in ['S', 'N']:
            print("Opção inválida! Tente novamente")
            cadastrar_agora = input("Deseja cadastrar um novo cliente agora? (S/N):").upper()

        if cadastrar_agora == 'S':
            cadastrar_cliente()
        
        else:
            print("Venda cancelada!")
            os.system('cls')
            main()

    produtos_venda = []
    valor_total = 0

    while True:
        produto_nome = input("Digite o nome do medicamento (ou 'sair' para finalizar a venda): ")

        if produto_nome.lower() == "sair":
            break

        produto = encontrar_medicamento_por_nome(produto_nome)
        if produto is None:
            print("Medicamento não encontrado.")
            continue

        produtos_venda.append(produto)
        valor_total += calcular_valor_produto(produto)

    desconto = calcular_desconto(cliente, valor_total)

    valor_total_com_desconto = valor_total - desconto
    data_hora = datetime.datetime.now()
    nova_venda = Venda(data_hora, produtos_venda, cliente, valor_total_com_desconto)
    vendas.append(nova_venda)
    
    print("Venda realizada com sucesso!")

# Funções auxiliares
def encontrar_cliente_por_cpf(cpf):
    for cliente in clientes:
        if cliente.cpf == cpf:
            return cliente
    return None

def encontrar_medicamento_por_nome(nome):
    for medicamento in medicamentos_quimio + medicamentos_fito:
        if nome.lower() in medicamento.nome.lower():
            return medicamento
    return None

def calcular_valor_produto(produto):
    # Implemente a lógica de cálculo do valor do produto
    pass

def calcular_desconto(cliente, valor_total):
    # Implemente a lógica de cálculo dos descontos
    pass

def exit():
    pass

if __name__ == "__main__":
    clientes = []
    medicamentos_quimio = []
    medicamentos_fito = []
    vendas = []
    laboratorios = []
    main()