from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

def get_db_connection():
    return pymysql.connect(
        host="servidor_bd",  # nombre del servicio MySQL en docker-compose
        user="root",
        password=os.environ.get("MYSQL_ROOT_PASSWORD"),  # ✅ variable de entorno segura
        database=os.environ.get("MYSQL_DATABASE"),
        port=3306,  # puerto interno de MySQL
        cursorclass=pymysql.cursors.DictCursor,
        connect_timeout=5  # evita que se quede colgado si MySQL tarda
    )

@app.route("/")
def home():
    return "Bienvenido a mi API con CI/CD 🚀"

@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT 1")
        conn.close()
        return jsonify({"status": "UP", "database": "UP"})
    except Exception as e:
        return jsonify({
            "status": "DOWN",
            "database": "DOWN",
            "error": str(e)
        }), 500

if __name__ == "__main__":
    docker_mode = os.environ.get("DOCKER_MODE", "false").lower() == "true"
    if docker_mode:
        app.run(host="0.0.0.0", port=5000)  # accesible desde fuera del contenedor
    else:
        app.run(host="127.0.0.1", port=5000)


