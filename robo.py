from serial.tools import list_ports
import inquirer
import pydobot
from yaspin import yaspin

class RoboController:
    def __init__(self):
        self.robo = None
        self.spinner = yaspin(text="Processando...", color="yellow")

    def escolher_porta_e_conectar(self):
        available_ports = list_ports.comports()
        if not available_ports:
            print("Nenhuma porta disponível encontrada.")
            return False
        porta_escolhida = inquirer.prompt([
            inquirer.List("porta", message="Escolha a porta serial", choices=[x.device for x in available_ports])
        ])["porta"]
        try:
            self.robo = pydobot.Dobot(port=porta_escolhida, verbose=False)
            self.configurar_parametros_iniciais()
            return True
        except Exception as e:
            print(f"Não foi possível conectar ao robô: {e}")
            return False
    
    def is_robot_connected(self):
        # Se self.robo não é None, assumimos que o robô está conectado
        return self.robo is not None

    def configurar_parametros_iniciais(self):
        self.robo.speed(30, 30)

    def mover_para(self, x, y, z):
        if self.robo:
            self.spinner.start()
            self.robo.move_to(x, y, z, 0, wait=True)
            self.spinner.stop()
            return True
        return False

    def sucção(self, ativar):
        if self.robo:
            self.spinner.start()
            self.robo.suck(ativar)
            self.robo.wait(200)
            self.spinner.stop()
            return True
        return False

    def finalizar(self):
        if self.robo:
            posicao_atual = self.robo.pose()
            print(f"Posição atual: {posicao_atual}")
            self.robo.close()

    def executar_sequencia_exemplo(self):
        if not self.robo:
            print("Robô não está conectado.")
            return

        # Sequência de movimentos de exemplo
        self.mover_para(200, 0, 0)
        self.sucção(True)
        self.mover_para(200, 200, 0)
        self.mover_para(0, 200, 0)
        self.sucção(False)

# Exemplo de uso
if __name__ == "__main__":
    controller = RoboController()
    if controller.escolher_porta_e_conectar():
        controller.executar_sequencia_exemplo()
        controller.finalizar()
