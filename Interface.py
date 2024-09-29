from cadastro import adicionar_cliente
from cadastro import adicionar_servico
from cadastro import agendar_servico
from cadastro import ver_agendamentos
from cadastro import ver_servicos
from cadastro import ver_agendamentos
from cadastro import ver_clientes


def menu():
    while True:
        print("\n==== MENU ====")
        print("1. Cadastrar Cliente")
        print("2. Cadastrar Serviço")
        print("3. Agendar Serviço")
        print("4. Ver Clientes")
        print("5. Ver Serviços")
        print("6. Ver Agendamentos")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Nome do Cliente: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            adicionar_cliente(nome, telefone, email)
        elif opcao == '2':
            nome = input("Nome do Serviço: ")
            preco = float(input("Preço: "))
            adicionar_servico(nome, preco)
        elif opcao == '3':
            cliente_id = int(input("ID do Cliente: "))
            servico_id = int(input("ID do Serviço: "))
            data = input("Data (dd-mm-aaaa): ")
            hora = input("Hora (hh:mm): ")
            agendar_servico(cliente_id, servico_id, data, hora)
        elif opcao == '4':
            ver_clientes()
        elif opcao == '5':
            ver_servicos()
        elif opcao == '6':
            ver_agendamentos()
        elif opcao == '7':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executar o menu
menu()
