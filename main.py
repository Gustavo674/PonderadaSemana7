from flask import Flask
import comands, logs

app = Flask(__name__)

app.register_blueprint(comands.router)
app.register_blueprint(logs.router)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=False)