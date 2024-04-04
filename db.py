from tinydb import TinyDB, Query
from datetime import datetime

db = TinyDB('db.json')

def get_all_logs():
    return db.all()

def log_command(command):
    command['timestamp'] = datetime.now().isoformat()
    db.insert(command)

def get_all_logs():
    return db.all()

def is_robot_connected():
    # Aqui você implementaria a lógica para verificar se o robô está conectado
    # Para simplificar, vou retornar True como se o robô estivesse sempre conectado
    return True
