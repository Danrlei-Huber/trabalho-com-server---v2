import Pyro5
import Pyro5.core
import Pyro5.server
from libs.server import veiculos_data

@Pyro5.server.expose
class VeiculosManager(object):
    def __init__(self):
        self.veiculos = veiculos_data.get_veiculos()

    def create(self, id_veiculo, marca, modelo, ano, preco):
        if id_veiculo in self.veiculos:
            return f"Veículo com ID {id_veiculo} já existe."
        self.veiculos[id_veiculo] = {
            'marca': marca,
            'modelo': modelo,
            'ano': ano,
            'preco': preco,
        }
        return f"Veículo {id_veiculo} criado com sucesso."

    def read(self, id_veiculo):
        veiculo = self.veiculos.get(id_veiculo)
        if veiculo:
            return veiculo
        return "Veículo não encontrado."

    def update(self, id_veiculo, marca=None, modelo=None, ano=None, preco=None):
        veiculo = self.veiculos.get(id_veiculo)
        if not veiculo:
            return "Veículo não encontrado."
        if marca:
            veiculo['marca'] = marca
        if modelo:
            veiculo['modelo'] = modelo
        if ano:
            veiculo['ano'] = ano
        if preco:
            veiculo['preco'] = preco
        return f"Veículo {id_veiculo} atualizado com sucesso."

    def delete(self, id_veiculo):
        if id_veiculo in self.veiculos:
            del self.veiculos[id_veiculo]
            return f"Veículo {id_veiculo} removido com sucesso."
        return "Veículo não encontrado."

    def read_all(self):
        if not self.veiculos:
            return "Nenhum veículo encontrado."
        
        return self.veiculos
    
    def __to_int(number):
        try:
            id_veiculo = int(id_veiculo)
        except ValueError:
            print("ID inválido. Deve ser um número inteiro.")
        

