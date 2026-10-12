import streamlit as st
import time

# Configuración de la página móvil
st.set_page_config(
    page_title="System Update",
    page_icon="⚙️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo visual estilo "Modo Seguro" oscuro usando HTML/CSS inofensivo
st.markdown("""
    <style>
    .reportview-container, .main {
        background-color: #0d0d0d;
        color: #ffffff;
        font-family: 'Courier New', Courier, monospace;
    }
    .stProgress > div > div > div > div {
        background-color: #ff3333;
    }
    h1, h3 {
        color: #ff3333;
        text-align: center;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 20px;
        width: 100%;
        text-align: center;
        color: #555555;
        font-size: 12px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("⚠️ ALERTA DE SISTEMA")
st.subheader("Optimizando almacenamiento y restaurando registros...")

# Mensaje de advertencia de broma
st.warning("No cierres el navegador ni bloquees el teléfono. Duración estimada: 2 minutos.")

# Contenedor para el texto del progreso
texto_progreso = st.empty()
# Barra de progreso visual
barra = st.progress(0)

# El temporizador dura 120 segundos (2 minutos)
duracion_total = 120 

for i in range(1, duracion_total + 1):
    porcentaje = int((i / duracion_total) * 100)
    tiempo_restante = duracion_total - i
    
    # Actualiza el texto en pantalla en tiempo real sin congelar nada
    texto_progreso.markdown(f"**Progreso:** {porcentaje}% | **Tiempo estimado:** {tiempo_restante} segundos.")
    barra.progress(porcentaje)
    
    # Pausa de 1 segundo por ciclo
    time.sleep(1)

# Al terminar los 2 minutos, borra todo y muestra el desenlace
st.empty()
st.balloons() # Animación festiva de Streamlit
st.success("### 🎉 ¡CAÍSTE! 🎉")
st.write("Tu teléfono está perfectamente bien. ¡Es solo una broma! 😂")

st.markdown('<div class="footer">[ Código de error: LAUGH-404 ]</div>', unsafe_allow_html=True)
