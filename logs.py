from flask import Blueprint, render_template
from tinydb import TinyDB

router = Blueprint('logs', __name__)

db = TinyDB("db.json")
logs_table = db.table("logs")

@router.route('/logs', methods=['GET'])
def get_logs():
    logs = db.all()
    return render_template('logs.html', logs=logs)