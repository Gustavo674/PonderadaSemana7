from flask import Blueprint, render_template  # Importa Blueprint e render_template do Flask
from tinydb import TinyDB  # Importa TinyDB para interação com banco de dados leve baseado em arquivo JSON

router = Blueprint('logs', __name__)  # Cria um Blueprint chamado 'logs' que será registrado no app Flask

db = TinyDB("db.json")  # Instancia um novo banco de dados TinyDB usando o arquivo db.json
logs_table = db.table("logs")  # Seleciona a tabela 'logs' dentro do banco de dados JSON

@router.route('/logs', methods=['GET'])  # Define a rota '/logs' para requisições GET
def get_logs():
    logs = db.all()  # Obtém todos os registros da tabela 'logs' no banco de dados
    return render_template('logs.html', logs=logs)  # Renderiza o template 'logs.html' passando os logs
