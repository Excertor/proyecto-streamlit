import streamlit as st
import pandas as pd

def opcion4(archivo):
   try:
        temperaturas= pd.DataFrame(archivo)
        return temperaturas['AvgTemperature'].min()
   except Exception:
         st.error(f"Error: No se cargo correctamente el archivo .csv, Intente nuevamente ingresando la ruta del archivo .csv en la opción 1")
         return None