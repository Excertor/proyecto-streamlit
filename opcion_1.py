import streamlit as st
import pandas as pd

def opcion1(ruta):
    if ruta:
         data_Temperatura= pd.read_csv(ruta)
         st.write(f"Archivo CSV leido exitosamente.")
         st.session_state.data_Temperatura = data_Temperatura
         return data_Temperatura