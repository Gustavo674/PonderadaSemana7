from flask import Flask, request, jsonify, render_template
from robo import RoboController
from db import get_all_logs, log_command  # Adicione a importação de log_command aqui

app = Flask(__name__)

# Inicializa uma instância global do controlador do robô.
robo_controller = RoboController()

@app.route('/')
def index():
    # Retorna uma página inicial simples para o controle do robô.
    return render_template('index.html', is_robot_connected=robo_controller.is_robot_connected())

@app.route('/logs')
def logs():
    """Endpoint para visualizar os logs do sistema."""
    all_logs = get_all_logs()
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

@app.route('/mover', methods=['POST'])
def mover():
    """Endpoint para mover o robô para uma posição especificada."""
    x = request.form.get('x')
    y = request.form.get('y')
    z = request.form.get('z')
    if not all([x, y, z]):
        return jsonify({'status': 'error', 'message': 'Coordenadas inválidas.'}), 400
    
    if robo_controller.mover_para(float(x), float(y), float(z)):
        log_command({'action': 'move', 'x': x, 'y': y, 'z': z})  # Registra a ação de mover
        return jsonify({'status': 'success', 'message': f'Movido para {x}, {y}, {z}.'})
    else:
        return jsonify({'status': 'error', 'message': 'Falha ao mover o robô.'}), 500

@app.route('/sucção', methods=['POST'])
def succao():
    """Endpoint para controlar a sucção do robô."""
    ativar = request.form.get('ativar', type=lambda x: x.lower() in ('true', 't', '1', 'yes'))
    if robo_controller.sucção(ativar):
        log_command({'action': 'suction', 'status': 'on' if ativar else 'off'})  # Registra a ação de sucção
        return jsonify({'status': 'success', 'message': f'Sucção {"ativada" if ativar else "desativada"}.'})
    else:
        return jsonify({'status': 'error', 'message': 'Falha ao controlar a sucção.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
