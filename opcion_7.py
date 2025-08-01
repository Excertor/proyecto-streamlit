import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def opcion7(archivo):
 
 data_archivoTemperatura = archivo
 DataFrame_archivoTemperatura = pd.DataFrame(data_archivoTemperatura)
  
 plt.figure(figsize=(6.5, 5.3))
 sns.histplot(DataFrame_archivoTemperatura['AvgTemperature'], bins=10)
 plt.title('Distribución de Temperaturas Promedio en Algiers, Enero 1995')
 plt.xlabel('Temperatura Promedio (°F)')
 plt.ylabel('Frecuencia')
 st.pyplot(plt)