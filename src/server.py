import Pyro5
import Pyro5.core
import Pyro5.server
import logging
from libs.server.VeiculosManager import VeiculosManager


def servidor():
    daemon = Pyro5.server.Daemon()
    uri = daemon.register(VeiculosManager)
    logging.info("Objeto servidor publicado.")
    logging.info(f"URI do objeto: {uri}")

    try:
        ns = Pyro5.core.locate_ns()
        logging.info("Conectado ao nameserver com sucesso!")
    except Exception as e:
        logging.error(f"Erro ao conectar ao nameserver: {e}")


    ns.register("VeiculosManager", uri)
    logging.info("Objeto registrado no servidor de nome.")

    logging.info("Executando request loop.")
    daemon.requestLoop()
    

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    servidor()
