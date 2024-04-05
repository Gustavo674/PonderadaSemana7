from flask import Blueprint, render_template, request, redirect, url_for # Importa classes e funções necessárias do Flask
from tinydb import TinyDB, Query # Importa TinyDB para operações com banco de dados e Query para consultas
from robot import RobotClass # Importa a classe RobotClass, que controla o robô
from datetime import datetime  # Importa datetime para manipular datas e horários

router = Blueprint('comandos', __name__) # Cria um novo Blueprint chamado 'comandos'

db = TinyDB("db.json") # Inicializa um banco de dados TinyDB usando 'db.json' como arquivo

comandos_table = db.table("logs") # Cria ou seleciona a tabela 'logs' no banco de dados

robo = RobotClass() # Cria uma instância da classe RobotClass que controla o robô

@router.route('/') # Define a rota raiz ('/') para requisições GET
def index():
    return render_template("index.html") # Renderiza o template 'index.html' quando a rota é acessada

@router.route('/movimentar', methods=['POST']) # Define a rota '/movimentar' para requisições POST
def movimentar():
    dados = request.json # Obtém dados JSON da requisição

    # Tenta obter as coordenadas x, y, z dos dados JSON
    x = dados.get('x')
    y = dados.get('y')
    z = dados.get('z')

    # Se qualquer coordenada for None (não fornecida), registra uma tentativa falha e redireciona para a index
    if x == None or y == None or z == None:
        registrar_comando("Movimento - Não foi possível movimentar o robô", x=x, y=y, z=z)
        return redirect(url_for('index.html'))
    else: # Se todas as coordenadas forem fornecidas
        x = float(x)
        y = float(y)
        z = float(z)
        registrar_comando("Movimento - Movimento realizado com sucesso", x=x, y=y, z=z)
        robo.move_to(x, y, z, 0) # Comanda o robô para se mover para as coordenadas especificadas
    
    return render_template('index.html') # Renderiza 'index.html' após a execução do comando

# A seguir, as rotas '/ligar-ferramenta' e '/desligar-ferramenta' funcionam de maneira semelhante.
# Elas obtêm os dados JSON da requisição, executam a ação correspondente (ligar/desligar a ferramenta)
# e registram o comando juntamente com a data e hora.

@router.route('/ligar-ferramenta', methods=['POST']) 
def ligar_ferramenta():
    dados = request.json 

    ligar = dados.get('ligar')

    if ligar == True:
        registrar_comando("Atuador - Ferramenta ligada com sucesso", ligar=ligar)
        robo.ligar_ferramenta()
    else:
        registrar_comando("Atuador - Não foi possível ligar a ferramenta", ligar=ligar)

    return render_template('index.html')

@router.route('/desligar-ferramenta', methods=['POST'])
def desligar_ferramenta():
    dados = request.json

    desligar = dados.get('desligar')

    if desligar == True:
        registrar_comando("Atuador - Ferramenta desligada com sucesso", desligar=desligar)
        robo.desligar_ferramenta()
    else:
        registrar_comando("Atuador - Não foi possível desligar a ferramenta", desligar=desligar)

    return render_template('index.html')

@router.route('/home', methods=['POST']) # Define a rota '/home' para requisições POST
def home():
    dados = request.json # Obtém dados JSON da requisição

    voltar = dados.get('voltar') # Obtém o valor da chave 'voltar' nos dados JSON

     # Se 'voltar' for True, move o robô para a posição inicial (casa) e registra o comando
    if voltar == True:
        robo.move_to(243.84, 5.12, 157.94, 0)
        registrar_comando("Home - O robô voltou para a casa com sucesso", voltar=voltar, x=243.84, y=5.12, z=157.94)
    else: # Se 'voltar' não for True, registra uma tentativa falha de voltar para a casa
        registrar_comando("Home - O robô não conseguiu voltar para a casa", voltar=voltar)

    return render_template('index.html') # Renderiza 'index.html' após a execução do comando

def registrar_comando(comando, **kwargs):
    now = datetime.now() # Obtém a data e hora atuais
    data_hora = now.strftime("%d/%m/%Y %H:%M:%S") # Formata a data e hora
    registro = {"comando": comando, "data_hora": data_hora} # Cria um registro com o comando e a data/hora
    registro.update(kwargs) # Atualiza o registro com quaisquer outros argumentos fornecidos
    db.insert(registro) # Insere o registro no banco de dados