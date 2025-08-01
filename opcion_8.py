import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def opcion8(archivo):

 data_archivoTemperatura = archivo
 DataFrame_archivoTemperatura = pd.DataFrame(data_archivoTemperatura)
 
 plt.figure(figsize=(10, 6))
 plt.plot(DataFrame_archivoTemperatura['Day'],DataFrame_archivoTemperatura['AvgTemperature'],linewidth=0)
 plt.scatter(DataFrame_archivoTemperatura['Day'],DataFrame_archivoTemperatura['AvgTemperature'])
 plt.xlabel('Día de Enero')
 plt.ylabel('Temperatura Promedio (°F)')
 plt.title('Temperatura Promedio vs. Día de Enero en Algiers, 1995')
 plt.grid(True)
 st.pyplot(plt.gcf())