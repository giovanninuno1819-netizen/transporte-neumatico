import streamlit as st
import math

st.set_page_config(page_title="Transporte Neumático", layout="wide")

st.title("Sistema de Transporte Neumático")
st.caption("Calculadora Industrial Básica para Ingeniería de Procesos")
st.divider()

st.header("Datos de Entrada")
col1, col2, col3 = st.columns(3)

with col1:
    masa_lote = st.number_input("Masa del lote (kg)", value=3360.0, step=100.0)
    tiempo_lote = st.number_input("Tiempo lote (min)", value=30.0, step=1.0)

with col2:
    diametro = st.number_input("Diámetro tubería (m)", value=0.102, format="%.3f", step=0.01)
    velocidad = st.number_input("Velocidad aire (m/s)", value=28.88, step=0.5)

with col3:
    longitud_horizontal = st.number_input("Longitud horizontal (m)", value=26.0, step=1.0)
    longitud_vertical = st.number_input("Longitud vertical (m)", value=15.0, step=1.0)
    erosion = st.number_input("Erosión codo (mm/h)", value=0.0113, format="%.4f", step=0.001)

st.divider()

kg_min = masa_lote / tiempo_lote
kg_hora = kg_min * 60
area_tuberia = math.pi * (diametro ** 2) / 4
caudal_aire = area_tuberia * velocidad
longitud_total = longitud_horizontal + longitud_vertical
limite_desgaste = 1.07
vida_util = limite_desgaste / erosion

st.header("Resultados del Sistema")
res_col1, res_col2, res_col3 = st.columns(3)
with res_col1:
    st.metric(label="Trasvase por Minuto", value=f"{kg_min:.2f} kg/min")
with res_col2:
    st.metric(label="Trasvase por Hora", value=f"{kg_hora:.2f} kg/h")
with res_col3:
    st.metric(label="Longitud Total de Línea", value=f"{longitud_total:.2f} m")

res_col4, res_col5, res_col6 = st.columns(3)
with res_col4:
    st.metric(label="Área de la Tubería", value=f"{area_tuberia:.5f} m²")
with res_col5:
    st.metric(label="Caudal de Aire", value=f"{caudal_aire:.5f} m³/s")
with res_col6:
    st.metric(label="Vida Útil Estimada (Codos)", value=f"{vida_util:.2f} h")

st.divider()

st.header("Diagnóstico Operacional")
diag_col1, diag_col2 = st.columns(2)

with diag_col1:
    st.subheader("Estado de la Velocidad")
    if velocidad < 18:
        st.warning("Riesgo de sedimentación: La velocidad es demasiado baja para mantener el producto en suspensión.")
    elif velocidad > 35:
        st.error("Riesgo alto de erosión: La velocidad excesiva acelerará el desgaste de la tubería.")
    else:
        st.success("Velocidad aceptable: Flujo seguro y dentro de parámetros.")

with diag_col2:
    st.subheader("Estado de Desgaste")
    if vida_util < 500:
        st.error("Vida útil baja: Se requiere programar mantenimiento preventivo a corto plazo para los codos.")
    else:
        st.success("Vida útil aceptable: Los codos resistirán un tiempo de operación adecuado.")

st.divider()
st.markdown("<div style='text-align: center; color: gray;'>Software desarrollado por Giovanni Nuño</div>", unsafe_allow_html=True)
