import Pyro5.api
import Pyro5.client
import Pyro5.errors
import sys
from time import sleep

def cliente():
    try:
        ns = Pyro5.api.locate_ns(host="localhost", port=9090)
    except Pyro5.errors.CommunicationError:
        print("Não foi possível localizar o servidor de nomes.")
        sys.exit()

    try:
        uri = ns.lookup("VeiculosManager")  # Nome do objeto registrado no servidor de nomes
        print(f"URI do objeto VeiculosManager: {uri}")
    except Pyro5.errors.PyroError:
        print("Não foi possível encontrar a URI do objeto VeiculosManager no servidor de nomes.")
        sys.exit()
    sleep(180)
    veiculos_manager = Pyro5.client.Proxy(uri)

    print("# Sistema de Gestão de Veículos #")

    while True:
        print("\nOperações disponíveis:")
        print("1. CREATE - Adicionar um veículo")
        print("2. READ - Buscar veículo por ID")
        print("3. UPDATE - Atualizar dados de um veículo")
        print("4. DELETE - Remover um veículo")
        print("5. READ-ALL - Listar todos os veículos")
        print("6. EXIT - Sair")

        escolha = input("Escolha uma operação: ").strip()

        if escolha == "1":
            id_veiculo = int(input("ID do veículo: ").strip())
            marca = input("Marca: ").strip()
            modelo = input("Modelo: ").strip()
            ano = input("Ano: ").strip()
            preco = float(input("Preço: ").strip())
            resposta = veiculos_manager.create(id_veiculo, marca, modelo, ano, preco)
            print(resposta)

        elif escolha == "2":
            id_veiculo = int(input("ID do veículo: ").strip())
            resposta = veiculos_manager.read(id_veiculo)
            print(resposta)

        elif escolha == "3":
            id_veiculo = int(input("ID do veículo a atualizar: ").strip())
            marca = input("Nova Marca: ").strip() or None
            modelo = input("Novo Modelo: ").strip() or None
            ano = input("Novo Ano: ").strip() or None
            preco = input("Novo Preço: ").strip()
            preco = float(preco) if preco else None
            resposta = veiculos_manager.update(id_veiculo, marca, modelo, ano, preco)
            print(resposta)

        elif escolha == "4":
            id_veiculo = int(input("ID do veículo a remover: ").strip())
            resposta = veiculos_manager.delete(id_veiculo)
            print(resposta)

        elif escolha == "5":
            resposta = veiculos_manager.read_all()
            print(resposta)

        elif escolha == "6":
            print("Encerrando cliente.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    cliente()
