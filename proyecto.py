import streamlit as st
import opcion_1 as uno
import opcion_2 as dos
import opcion_3 as tres
import opcion_4 as cuatro
import opcion_5 as cinco
import opcion_6 as seis
import opcion_7 as siete
import opcion_8 as ocho
import opcion_9 as nueve

st.markdown(""" <style> body {background-color: black; color: white;} </style>""", unsafe_allow_html=True,)
st.header("--- Explorador de Datos Climáticos ---")
st.subheader("1. Leer Datos Climáticos desde CSV")
st.subheader("2. Calcular Promedio de Temperatura Promedio")
st.subheader("3. Encontrar Temperatura Promedio Máxima")                                                    
st.subheader("4. Encontrar Temperatura Promedio Mínima")                                                 
st.subheader("5. Filtrar registros con Temperatura Promedio mayor a un valor")                                                        
st.subheader("6. Filtrar registros con Temperatura Promedio menor a un valor")                                                        
st.subheader("7. Generar Histograma de Temperaturas Promedio")                                                       
st.subheader("8. Genera un gráfico de dispersión del Día vs. Temperatura Promedio.")                                                       
st.subheader("9. Mostrar Datos Ingresados")                                                    
st.subheader("0. Salir")
st.header("------------------------------------")
    
try:
    opcion = st.selectbox("Seleccione una opción: ",[1,2,3,4,5,6,7,8,9,0])
    if opcion == 0:
            st.write("Saliendo del Explorador de Datos Climáticos. ¡Hasta Luego!")
    elif opcion == 1:
          try:
            ruta=st.file_uploader("Ingrese la ruta del archivo .csv con los datos climáticos: ", type="csv")
            archivo = uno.opcion1(ruta)
          except Exception as d_e:
           st.error(f"Error: No se encontró el archivo .csv, en la ruta especificada: {d_e}")
    elif opcion == 2 and ("data_Temperatura" in st.session_state):
                   st.write(f"Promedio de Temperatura Promedio: {dos.opcion2(st.session_state.data_Temperatura)} °F")
    elif opcion == 3 and ("data_Temperatura" in st.session_state):
            st.write(f"Temperatura Promedio Máxima registrada: {tres.opcion3(st.session_state.data_Temperatura)} °F")
    elif opcion == 4 and ("data_Temperatura" in st.session_state):
            st.write(f"Temperatura Promedio Mínima registrada: {cuatro.opcion4(st.session_state.data_Temperatura)} °F")
    elif opcion == 5 and ("data_Temperatura" in st.session_state):
            try:
                temperatura = st.number_input("Ingrese el límite de temperatura promedio: ", value=None)
                if temperatura is not None:
                        st.write(f"\nRegistros con Temperatura Promedio mayor a {temperatura} °F:")           
                        cinco.opcion5(st.session_state.data_Temperatura, temperatura)
            except:
                st.error("Limite de temperatura ingresado invalido, intente de nuevo")
    elif opcion == 6 and ("data_Temperatura" in st.session_state):
            try:
                temperatura = st.number_input("Ingrese el límite de temperatura promedio: ", value=None)
                if temperatura is not None:
                        st.write(f"\nRegistros con Temperatura Promedio menor a {temperatura} °F:")
                        seis.opcion6(st.session_state.data_Temperatura, temperatura)
            except:
                st.error("Limite de temperatura ingresado invalido, intente de nuevo")
    elif opcion ==  7 and ("data_Temperatura" in st.session_state):
            siete.opcion7(st.session_state.data_Temperatura)
    elif opcion==  8 and ("data_Temperatura" in st.session_state):
            ocho.opcion8(st.session_state.data_Temperatura)
    elif opcion== 9 and ("data_Temperatura" in st.session_state):
            st.write("Datos Ingresados:")
            st.write(nueve.opcion9(st.session_state.data_Temperatura))
    else:
            st.error("Error. El archivo no ha sido cargado correctamente")
            

except ValueError:

        st.error("Opción inválida. Por favor, seleccione una opción del menú.")
