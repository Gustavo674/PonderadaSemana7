from flask import Flask, request, jsonify, render_template
from robo import RoboController
from db import get_all_logs

app = Flask(__name__)

# Inicializa uma instância global do controlador do robô.
robo_controller = RoboController()

@app.route('/')
def index():
    # Retorna uma página inicial simples para o controle do robô.
    return render_template('index.html')

@app.route('/logs')
def logs():
    """Endpoint para visualizar os logs do sistema."""
    all_logs = get_all_logs()  # Certifique-se de que essa função retorne os logs corretamente
    return render_template('logs.html', logs=all_logs)

@app.route('/control')
def control():
    """Endpoint para a página de controle do robô."""
    return render_template('control.html', is_robot_connected=robo_controller.is_robot_connected())

@app.route('/conectar', methods=['POST'])
def conectar():
    """Endpoint para conectar ao robô."""
    if robo_controller.escolher_porta_e_conectar():
        return jsonify({'status': 'success', 'message': 'Robô conectado com sucesso.'})
    else:
        return jsonify({'status': 'error', 'message': 'Falha ao conectar com o robô.'}), 500

def logs():
    all_logs = get_all_logs()
    return render_template('logs.html', logs=all_logs)

@app.route('/mover', methods=['POST'])
def mover():
    """Endpoint para mover o robô para uma posição especificada."""
    data = request.json
    x = data.get('x')
    y = data.get('y')
    z = data.get('z')
    if x is None or y is None or z is None:
        return jsonify({'status': 'error', 'message': 'Coordenadas inválidas.'}), 400

    if robo_controller.mover_para(x, y, z):
        return jsonify({'status': 'success', 'message': f'Movido para {x}, {y}, {z}.'})
    else:
        return jsonify({'status': 'error', 'message': 'Falha ao mover o robô.'}), 500

@app.route('/sucção', methods=['POST'])
def succao():
    """Endpoint para controlar a sucção do robô."""
    data = request.json
    ativar = data.get('ativar', False)
    if robo_controller.sucção(ativar):
        acao = "ativada" if ativar else "desativada"
        return jsonify({'status': 'success', 'message': f'Sucção {acao}.'})
    else:
        return jsonify({'status': 'error', 'message': 'Falha ao controlar a sucção.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
