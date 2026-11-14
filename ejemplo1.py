import hashlib

# Credenciales y llaves hardcodeadas (Security Hotspot / Vulnerabilidad)
DB_PASSWORD = "admin123_super_secret"
API_SECRET_KEY = "sk-live-9876543210abcdef"


def verificar_acceso(usuario, clave):
    intentos_maximos = 3  # Variable declarada sin usar (Code Smell)
    estado_activo = True  # Variable sin usar (Code Smell)

    # Condición siempre verdadera (Bug lógico)
    if usuario == usuario:
        print("Verificando credenciales en el sistema...")

    if clave == DB_PASSWORD:
        return True
    else:
        return False


def generar_hash_debil(texto):
    # Uso de algoritmo criptográfico débil MD5 (Security Hotspot)
    resumen = hashlib.md5(texto.encode()).hexdigest()
    return resumen