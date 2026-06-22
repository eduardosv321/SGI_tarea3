import streamlit as st
from modulos.config.conexion import obtener_conexion
 from modulos. ventas import mostrar_venta

def verificar_usuario(Nombre, Contraseña):
    con = obtener_conexion()
    if not con:
        st.error("⚠️ No se pudo conectar a la base de datos.")
        return None
    else:
        # ✅ Guardar en el estado que la conexión fue exitosa
        st.session_state["conexion_exitosa"] = True

    try:
        cursor = con.cursor()
        query = "SELECT Nombre, Contraseña FROM Usuarios WHERE Nombre = %s AND Contraseña = %s"
        cursor.execute(query, (Nombre, Contraseña))
        result = cursor.fetchone()
        return result[0] if result else None
    finally:
        con.close()


def login():
    st.title("Inicio de sesión")

    # 🟢 Mostrar mensaje persistente si ya hubo conexión exitosa
    if st.session_state.get("conexion_exitosa"):
        st.success("✅ Conexión a la base de datos establecida correctamente.")

    Nombre = st.text_input("Nombre", key="nombre_input")
    Contraseña = st.text_input("Contraseña", type="password", key="Contraseña_input")

    if st.button("Iniciar sesión"):
        tipo = verificar_usuario(Nombre, Contraseña)
        if tipo:
            st.session_state["Nombre"] = Nombre
            st.session_state["tipo_nombre"] = tipo
            st.success(f"Bienvenido ({Nombre}) 👋")
            st.session_state["sesion_iniciada"] = True
            st.rerun()
        else:
            st.error("❌ Credenciales incorrectas.")
