import streamlit as st
import pandas as pd

def opcion2(archivo):
    try:
        temperaturas= pd.DataFrame(archivo)
        Promedio_de_Temperatura_Promedio=temperaturas['AvgTemperature'].mean()
        return round(Promedio_de_Temperatura_Promedio, 2)
    except Exception:
         st.error(f"Error: No se cargo correctamente el archivo .csv, Intente nuevamente ingresando la ruta del archivo .csv en la opción 1")
         return None