import socket
import logging
from libs.server.VeiculosManager import VeiculosManager


def servidor():
    host = 'localhost'
    porta = 5000
    veiculos_manager = VeiculosManager()

    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor_socket.bind((host, porta))
    servidor_socket.listen(1)

    logging.info(f"Servidor ouvindo em {host}:{porta}")

    conn, addr = servidor_socket.accept()
    logging.info(f"Conexão de {addr}")

    while True:
        dados_tam = conn.recv(2)
        if not dados_tam:
            logging.warning("Conexão encerrada pelo cliente")
            break

        tam_msg = int.from_bytes(dados_tam, 'big')
        dados = conn.recv(tam_msg).decode()
        logging.info(f"Dados recebidos: {dados}")
        if not dados:
            logging.warning("Sem dados recebidos")
            break

        partes = dados.strip('#').split('|')
        operacao = partes[0]
        resposta = "Comando inválido."

        try:
            if operacao == "CREATE":
                id_veiculo = int(partes[1])
                marca = partes[2]
                modelo = partes[3]
                ano = int(partes[4])
                preco = float(partes[5])
                resposta = veiculos_manager.create(id_veiculo, marca, modelo, ano, preco)

            elif operacao == "READ":
                id_veiculo = int(partes[1])
                resposta = veiculos_manager.read(id_veiculo)

            elif operacao == "UPDATE":
                id_veiculo = int(partes[1])
                marca = partes[2] if partes[2] else None
                modelo = partes[3] if partes[3] else None
                ano = int(partes[4]) if partes[4] != "0" else None
                preco = float(partes[5]) if partes[5] != "0.0" else None
                resposta = veiculos_manager.update(id_veiculo, marca, modelo, ano, preco)

            elif operacao == "DELETE":
                id_veiculo = int(partes[1])
                resposta = veiculos_manager.delete(id_veiculo)

            elif operacao == "READ-ALL":
                resposta = veiculos_manager.read_all()

            elif operacao == "EXIT":
                resposta = "Encerrando conexão."
                conn.send(len(resposta.encode()).to_bytes(2, 'big') + resposta.encode())
                break

        except (IndexError, ValueError) as e:
            resposta = "Formato inválido."

        resposta_bytes = resposta.encode()
        tam_resposta = len(resposta_bytes).to_bytes(2, 'big')
        conn.send(tam_resposta + resposta_bytes)

    conn.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    servidor()
