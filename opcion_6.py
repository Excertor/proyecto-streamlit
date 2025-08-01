import streamlit as st
import pandas as pd

def opcion6(archivo, limite):
 try:
     minimo_valor=limite
     temperaturas= pd.DataFrame(archivo)
     lista_que_contiene_al_limite=temperaturas[temperaturas['AvgTemperature'] < minimo_valor]
     lista_diccionarios= lista_que_contiene_al_limite.to_dict(orient='records')
     if len(lista_diccionarios) > 0:
      for diccionarios in lista_diccionarios:
       st.write(f"{diccionarios}")
     else:
       st.info(f"No se han encontrado registros con Temperatura Promedio menor a {minimo_valor} °F")
 except Exception:
        st.error(f"Error: No se cargo correctamente el archivo .csv, Intente nuevamente ingresando la ruta del archivo .csv en la opción 1")