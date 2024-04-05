from pydobot import Dobot
from serial.tools import list_ports

class RobotClass:
    # Inicializando o robô
    def __init__(self):
        self.port = self.scan_ports()
        self.robo = Dobot(port=self.port)
        self.robo.speed(100, 100)
        posicao_atual = self.robo.pose()    
        print(f"Posição inicial {posicao_atual}")

    # Função para pegar a posição atual do robô
    def posição_atual(self):
        return self.robo.pose()

    # Função para mover o robô para uma posição específica
    def move_to(self, x, y, z, r, wait=True):
        self.robo.move_to(x, y, z, r)

    # Função para ligar a ferramenta
    def ligar_ferramenta(self):
        self.robo.suck(True)
    
    # Função para desligar a ferramenta 
    def desligar_ferramenta(self):
        self.robo.suck(False)

    # Função para escanear as portas e encontrar o robô
    def scan_ports(self):
        ports = list_ports.comports()
        for port in ports:
            print(f"Trying port {port.device}")
            try:
                robot = Dobot(port=port.device)
                robot.close()
                print(f"Found robot at {port.device}")
                return port.device
            except:
                print(f"No robot found at {port.device}")
        raise Exception("No robot found")