# app.py

import streamlit as st
from modulos.ventas import mostrar_venta
from modulos.login import login

# Comprobamos si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:

    # Mostrar el menú lateral
    opciones = ["ventas", "Otra opción"]
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    # Según la opción seleccionada, mostramos el contenido correspondiente
    if seleccion == "ventas":
        mostrar_venta()

    elif seleccion == "Otra opción":
        st.write("Has seleccionado otra opción.")

else:
    # Si la sesión no está iniciada, mostrar el login
    login()
