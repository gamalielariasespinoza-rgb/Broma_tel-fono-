import streamlit as st
import time
import random

# Configuración de página móvil estilo terminal secreta
st.set_page_config(
    page_title="System Breach Detected",
    page_icon="💀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Estilo visual avanzado: Fondo negro, texto verde de consola y alertas rojas parpadeantes
st.markdown("""
    <style>
    .reportview-container, .main {
        background-color: #050505 !important;
        color: #00ff00 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    .stProgress > div > div > div > div {
        background-color: #ff0000 !important;
    }
    .titulo-alerta {
        color: #ff0000;
        text-align: center;
        font-size: 24px;
        font-weight: bold;
        text-shadow: 0 0 10px #ff0000;
        animation: parpadeo 1s infinite;
    }
    .log-terminal {
        background-color: #111;
        padding: 15px;
        border-radius: 5px;
        border: 1px solid #333;
        font-size: 13px;
        color: #00dd00;
        height: 250px;
        overflow-y: hidden;
    }
    @keyframes parpadeo {
        0% { opacity: 1; }
        50% { opacity: 0.3; }
        100% { opacity: 1; }
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado alarmante
st.markdown('<div class="titulo-alerta">💀 THREAT DETECTED: TROJAN.ANDROID.OS 💀</div>', unsafe_allow_html=True)
st.write("")
st.subheader("Extrayendo paquetes de datos y volcando memoria caché...")

# Lista de procesos falsos que simulan el hackeo
falsos_logs = [
    " Connecting to external proxy server... DONE",
    " Accessing root permissions... GRANTED",
    " Bypassing Android Security Sandbox...",
    " Encrypting local files (/sdcard/DCIM/)...",
    " Downloading background payload: exploit_v4.bin",
    " Mirroring contact list to remote server...",
    " Overriding system kernel protocols...",
    " Deleting system_manifest.xml...",
    " Warning: CPU temperature rising...",
    " Injecting malware into internal storage...",
    " Copying active session tokens (WhatsApp, Google)...",
    " Disabling remote device tracking..."
]

# Contenedor dinámico para la consola
consola_html = st.empty()
# Barra de progreso
barra = st.progress(0)

duracion_total = 60 # Reducido a 60 segundos (1 minuto) para que sea más rápida e intensa
logs_acumulados = []

for i in range(1, duracion_total + 1):
    porcentaje = int((i / duracion_total) * 100)
    
    # Cada ciertos segundos añade un texto de sistema aleatorio para que parezca real
    if i % 5 == 0 and len(falsos_logs) > 0:
        nuevo_log = falsos_logs.pop(random.randint(0, len(falsos_logs)-1))
        logs_acumulados.append(f"[SYS_ERR] {nuevo_log}")
    
    # Rellenar la consola visual con las últimas líneas de código falsas
    texto_consola = "<br>".join(logs_acumulados[-8:]) # Muestra las últimas 8 líneas
    consola_html.markdown(f'<div class="log-terminal">{texto_consola}<br>📡 Enviando paquetes... {porcentaje}%</div>', unsafe_allow_html=True)
    
    barra.progress(porcentaje)
    time.sleep(1)

# Pantalla final: Revela la broma de golpe
st.empty()
st.balloons()
st.success("### 🎉 ¡Broma completa! 🎉")
st.write("### Tu teléfono está 100% a salvo. ¡Caíste en la trampa! 😂")
    
