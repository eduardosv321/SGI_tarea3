# app.py

import streamlit as st
from modulos.ventas import mostrar_venta
from modulos.entradas import mostrar_entrada
from modulos.login import login

# Comprobamos si la sesión ya está iniciada
if "sesion_iniciada" in st.session_state and st.session_state["sesion_iniciada"]:

    # Menú lateral
    opciones = ["ventas", "entrada", "Otra opción"]
    seleccion = st.sidebar.selectbox("Selecciona una opción", opciones)

    # Mostrar el módulo correspondiente
    if seleccion == "ventas":
        mostrar_venta()

    elif seleccion == "entrada":
        mostrar_entrada()

    elif seleccion == "Otra opción":
        st.write("Has seleccionado otra opción.")

else:
    login()
