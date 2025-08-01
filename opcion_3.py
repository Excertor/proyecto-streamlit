import streamlit as st
import pandas as pd

def opcion3(archivo):
    try:
        temperaturas= pd.DataFrame(archivo)
        return temperaturas['AvgTemperature'].max()
    except Exception:
         st.error(f"Error: No se cargo correctamente el archivo .csv, Intente nuevamente ingresando la ruta del archivo .csv en la opción 1")
         return None