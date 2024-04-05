from pydobot import Dobot  # Importa a classe Dobot do módulo pydobot
from serial.tools import list_ports  # Importa a função list_ports do módulo serial.tools

class RobotClass:
    # Método construtor da classe RobotClass
    def __init__(self):
        self.port = self.scan_ports()  # Escaneia as portas e guarda a porta do Dobot
        self.robo = Dobot(port=self.port)  # Cria uma instância do Dobot na porta encontrada
        self.robo.speed(100, 100)  # Define a velocidade do robô
        posicao_atual = self.robo.pose()  # Obtém a pose atual do robô (posição + ângulos dos eixos)
        print(f"Posição inicial {posicao_atual}")  # Imprime a posição inicial do robô

    # Método para obter a posição atual do robô
    def posição_atual(self):
        return self.robo.pose()  # Retorna a pose atual do robô

    # Método para mover o robô para uma posição específica
    def move_to(self, x, y, z, r, wait=True):
        self.robo.move_to(x, y, z, r, wait=wait)  # Move o robô para as coordenadas (x, y, z) e rotação r

    # Método para ligar a ferramenta (ex: ventosa)
    def ligar_ferramenta(self):
        self.robo.suck(True)  # Ativa a ferramenta de sucção

    # Método para desligar a ferramenta (ex: ventosa)
    def desligar_ferramenta(self):
        self.robo.suck(False)  # Desativa a ferramenta de sucção

    # Método para escanear as portas seriais disponíveis e localizar o robô
    def scan_ports(self):
        ports = list_ports.comports()  # Lista todas as portas COM disponíveis
        for port in ports:  # Itera sobre as portas encontradas
            print(f"Trying port {port.device}")
            try:
                robot = Dobot(port=port.device)  # Tenta criar uma instância do Dobot na porta atual
                robot.close()  # Fecha a conexão imediatamente após a verificação bem-sucedida
                print(f"Found robot at {port.device}")
                return port.device  # Retorna o dispositivo da porta onde o robô foi encontrado
            except:
                print(f"No robot found at {port.device}")  # Imprime uma mensagem se não encontrar o robô
        raise Exception("No robot found")  # Levanta uma exceção se o robô não for encontrado em nenhuma porta
