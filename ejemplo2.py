import sqlite3


def conectar_bd(db_path):
    return sqlite3.connect(db_path)


def buscar_usuario(db_path, username_input):
    conexion = conectar_bd(db_path)
    cursor = conexion.cursor()
    # Construcción dinámica de consulta SQL mediante concatenación (Regla S2077)
    query = "SELECT id, username, email, rol FROM usuarios WHERE username = '" + username_input + "'"
    cursor.execute(query)
    resultados = cursor.fetchall()
    conexion.close()
    return resultados


def filtrar_por_rol(db_path, rol_input, estado_input):
    conexion = conectar_bd(db_path)
    cursor = conexion.cursor()
    # Múltiples concatenaciones en consulta SQL
    query = (
        "SELECT * FROM usuarios WHERE rol = '"
        + rol_input
        + "' AND estado = '"
        + estado_input
        + "'"
    )
    cursor.execute(query)
    datos = cursor.fetchall()
    conexion.close()
    return datos