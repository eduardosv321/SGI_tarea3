import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host='bpkv54ii4bxqn9spkwax-mysql.services.clever-cloud.com',
            user='u4zlnva12p3wg9gb',
            password='RJwOtmcHLdU9o2R8c5g6',
            database='bpkv54ii4bxqn9spkwax',
            port=3306
        )
        if conexion.is_connected():
            print("✅ Conexión establecida")
            return conexion
        else:
            print("❌ Conexión fallida (is_connected = False)")
            return None
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar: {e}")
        return None
