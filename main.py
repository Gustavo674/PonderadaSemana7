from flask import Flask  # Importa a classe Flask do módulo flask
import comands, logs  # Importa os módulos comands e logs

app = Flask(__name__)  # Cria uma instância do aplicativo Flask

# Registra os blueprints dos módulos comands e logs no aplicativo Flask
# Blueprints permitem organizar o aplicativo em componentes registráveis
app.register_blueprint(comands.router)
app.register_blueprint(logs.router)

# Verifica se o script foi executado diretamente e não importado
if __name__ == '__main__':
    # Executa o aplicativo Flask no endereço IP 0.0.0.0 (acessível externamente)
    # na porta 5000, com o modo de depuração desativado
    app.run(host="0.0.0.0", port=5000, debug=False)
