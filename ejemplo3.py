import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)
DATABASE = "app_empresa.db"


def obtener_conexion():
    return sqlite3.connect(DATABASE)


@app.route("/usuario", methods=["GET"])
def buscar_usuario():
    # Fuente de entrada no confiable (Source)
    username = request.args.get("username", "")
    filtro_limpio = username.strip()  # Propagación del dato contaminado (Taint)

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Sumidero peligroso: el dato llega sin sanitizar a la consulta (Regla S3649)
    query = "SELECT id, username, correo FROM usuarios WHERE username = '" + filtro_limpio + "'"
    cursor.execute(query)
    filas = cursor.fetchall()
    conexion.close()

    return jsonify({"usuarios": filas})


@app.route("/productos/buscar", methods=["GET"])
def buscar_producto():
    # Segunda fuente no confiable por parámetro URL
    categoria = request.args.get("categoria", "")
    orden = request.args.get("orden", "ASC")

    conexion = obtener_conexion()
    cursor = conexion.cursor()

    # Flujo de datos contaminado hacia consulta SQL dinámica (Regla S3649)
    sql = (
        "SELECT nombre, precio, stock FROM productos WHERE categoria = '"
        + categoria
        + "' ORDER BY precio "
        + orden
    )
    cursor.execute(sql)
    productos = cursor.fetchall()
    conexion.close()

    return jsonify({"resultados": productos})


if __name__ == "__main__":
    app.run(debug=True)  # Configuración insegura en producción (Security Hotspot)