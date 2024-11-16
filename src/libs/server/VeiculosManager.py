
from libs.server import veiculos_data


class VeiculosManager:
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
            return (
                f"Veículo encontrado:\n"
                f"Marca: {veiculo['marca']}\n"
                f"Modelo: {veiculo['modelo']}\n"
                f"Ano: {veiculo['ano']}\n"
                f"Preço: R${veiculo['preco']:.2f}"
            )
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
        lista_veiculos = [
            (
                f"ID: {id_veiculo} | "
                f"Marca: {v['marca']} | "
                f"Modelo: {v['modelo']} | "
                f"Ano: {v['ano']} | "
                f"Preço: R${v['preco']:.2f}"
            )
            for id_veiculo, v in self.veiculos.items()
        ]
        return "\n".join(lista_veiculos)

