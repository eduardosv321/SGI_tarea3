import streamlit as st
from modulos.config.conexion import obtener_conexion

def mostrar_entrada():
    st.header("📦 Registrar entrada de productos")

    try:
        con = obtener_conexion()
        cursor = con.cursor()

        # Formulario para registrar la entrada
        with st.form("form_entrada"):
            producto = st.text_input("Nombre del producto")
            cantidad = st.number_input("Cantidad", min_value=1, step=1)
            proveedor = st.text_input("Proveedor")

            enviar = st.form_submit_button("✅ Guardar entrada")

            if enviar:
                if producto.strip() == "":
                    st.warning("⚠️ Debes ingresar el nombre del producto.")
                elif proveedor.strip() == "":
                    st.warning("⚠️ Debes ingresar el proveedor.")
                else:
                    try:
                        cursor.execute(
                            """
                            INSERT INTO Entrada_Productos
                            (Producto, Cantidad, Proveedor)
                            VALUES (%s, %s, %s)
                            """,
                            (producto, str(cantidad), proveedor)
                        )

                        con.commit()

                        st.success(
                            f"✅ Entrada registrada correctamente: "
                            f"{producto} (Cantidad: {cantidad}) - Proveedor: {proveedor}"
                        )

                        st.rerun()

                    except Exception as e:
                        con.rollback()
                        st.error(f"❌ Error al registrar la entrada: {e}")

        # Mostrar registros existentes
        st.subheader("📋 Entradas registradas")

        cursor.execute("""
            SELECT id_entrada, Producto, Cantidad, Proveedor
            FROM Entrada_Productos
            ORDER BY id_entrada DESC
        """)

        registros = cursor.fetchall()

        if registros:
            st.table(registros)
        else:
            st.info("No hay entradas registradas.")

    except Exception as e:
        st.error(f"❌ Error general: {e}")

    finally:
        if 'cursor' in locals():
            cursor.close()

        if 'con' in locals():
            con.close()
