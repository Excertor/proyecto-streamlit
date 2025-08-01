import streamlit as st
import pandas as pd

def opcion9(archivo):
  try:
     temperaturas= pd.DataFrame(archivo)
     lista_diccionarios= temperaturas.to_dict(orient='records')
     for diccionarios in lista_diccionarios:
      st.write(f"{diccionarios}")
     return " "
  except Exception:
        st.error(f"Error: No se cargo correctamente el archivo .csv, Intente nuevamente ingresando la ruta del archivo .csv en la opción 1")
