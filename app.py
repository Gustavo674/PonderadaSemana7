from flask import Flask, render_template, request, redirect, url_for
from db import log_command, get_all_logs, is_robot_connected

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', is_robot_connected=is_robot_connected())

@app.route('/control', methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        # Aqui você capturaria os comandos enviados para o robô
        # Exemplo: log_command({'command': 'move', 'value': '50mm'})
        pass
    return render_template('control.html', is_robot_connected=is_robot_connected())

@app.route('/logs')
def logs():
    all_logs = get_all_logs()
    return render_template('logs.html', logs=all_logs)

if __name__ == '__main__':
    app.run(debug=True)
