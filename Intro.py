import streamlit as st
from PIL import Image, ImageOps

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS ORIGINAL
# ============================================================

st.markdown("""
<style>

    .stApp {
        background:
            radial-gradient(
                circle at top left,
                #312e81 0%,
                transparent 35%
            ),
            radial-gradient(
                circle at top right,
                #0e7490 0%,
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #0f172a,
                #111827 55%,
                #1e1b4b
            );
        color: #f8fafc;
    }

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #0f172a 0%,
                #172554 50%,
                #1e1b4b 100%
            );
        border-right: 1px solid rgba(255,255,255,0.12);
    }

    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: white !important;
    }

    section[data-testid="stSidebar"] p {
        color: #cbd5e1 !important;
        line-height: 1.7;
    }

    .titulo-principal {
        text-align: center;
        font-size: 3rem;
        font-weight: 900;
        margin-top: 15px;
        margin-bottom: 5px;
        background: linear-gradient(
            90deg,
            #38bdf8,
            #818cf8,
            #c084fc,
            #f472b6
        );
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .subtitulo-principal {
        text-align: center;
        color: #cbd5e1;
        font-size: 1.15rem;
        margin-bottom: 30px;
    }

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 20px;
        padding: 10px;
        box-shadow: 0 12px 30px rgba(0,0,0,0.30);
        margin-bottom: 25px;
    }

    .titulo-tarjeta {
        color: #f8fafc !important;
        font-size: 21px !important;
        font-weight: 750 !important;
        line-height: 1.25;
        min-height: 55px;
    }

    .numero {
        color: white;
        background: linear-gradient(
            135deg,
            #38bdf8,
            #6366f1
        );
        display: inline-block;
        padding: 5px 12px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 8px;
    }

    .descripcion {
        color: #cbd5e1 !important;
        font-size: 15px;
        line-height: 1.6;
        min-height: 95px;
        padding-top: 8px;
    }

    .stLinkButton a {
        background: linear-gradient(
            135deg,
            #2563eb,
            #7c3aed
        ) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        font-weight: 700 !important;
    }

    .stLinkButton a:hover {
        background: linear-gradient(
            135deg,
            #1d4ed8,
            #6d28d9
        ) !important;
        color: white !important;
    }

    [data-testid="stImage"] img {
        border-radius: 14px;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        padding: 35px 0 20px 0;
        font-size: 14px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNCIÓN PARA MOSTRAR TARJETAS
# ============================================================

def mostrar_tarjeta(
    numero,
    titulo,
    imagen,
    descripcion,
    texto_enlace,
    url
):
    with st.container(border=True):

        st.markdown(
            f'<div class="numero">Aplicación {numero}</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            f'<div class="titulo-tarjeta">{titulo}</div>',
            unsafe_allow_html=True
        )

        try:
            img = Image.open(imagen)

            img = ImageOps.fit(
                img,
                (600, 300),
                method=Image.Resampling.LANCZOS
            )

            st.image(
                img,
                use_container_width=True
            )

        except Exception:
            st.warning(
                f"No se pudo cargar la imagen: {imagen}"
            )

        st.markdown(
            f'<div class="descripcion">{descripcion}</div>',
            unsafe_allow_html=True
        )

        if url:
            st.link_button(
                f"🚀 {texto_enlace}",
                url,
                use_container_width=True
            )


# ============================================================
# ENCABEZADO
# ============================================================

st.markdown(
    '<div class="titulo-principal">'
    '🤖 Aplicaciones de Inteligencia Artificial'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo-principal">'
    'Explora diferentes herramientas y aplicaciones '
    'desarrolladas con Inteligencia Artificial'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🤖 Inteligencia Artificial")
    st.divider()

    st.markdown("### 📚 Sobre este proyecto")

    st.write(
        "La inteligencia artificial permite mejorar la toma "
        "de decisiones mediante el uso de datos, automatizar "
        "tareas rutinarias y proporcionar análisis avanzados "
        "en tiempo real."
    )

    st.divider()

    st.markdown("### 🧠 Aplicaciones disponibles")

    st.write("🎙️ Texto y voz")
    st.write("📝 Procesamiento de texto")
    st.write("👁️ Visión artificial")
    st.write("😊 Reconocimiento de emociones")
    st.write("🎯 Detección de objetos")
    st.write("☁️ Análisis de palabras")
    st.write("🤖 Machine Learning")


# ============================================================
# RECURSOS Y EJERCICIOS
# ============================================================

st.info(
    "📖 **Recursos y ejercicios**\n\n"
    "En el siguiente enlace puedes encontrar páginas, "
    "recursos y ejercicios prácticos relacionados con "
    "las aplicaciones de Inteligencia Artificial."
)

st.link_button(
    "🌐 Ver recursos y ejercicios",
    "https://sites.google.com/view/aplicacionesdeia/inicio",
    use_container_width=True
)

st.write("")


# ============================================================
# LISTA DE APLICACIONES
# ============================================================

aplicaciones = [

    # APLICACIONES ORIGINALES

    {
        "numero": 1,
        "titulo": "Introducción",
        "imagen": "inttro.jpg",
        "descripcion": "En esta aplicación se presenta una introducción a las aplicaciones de la Inteligencia Artificial.",
        "texto_enlace": "Introducción",
        "url": "https://estesi-z29ropifyfvwhuted9mfsb.streamlit.app/"
    },
    {
        "numero": 2,
        "titulo": "Conversión de texto a voz",
        "imagen": "texttospeech.jpg",
        "descripcion": "Aplicación que permite convertir texto escrito en voz mediante Inteligencia Artificial.",
        "texto_enlace": "Texto a voz",
        "url": "https://ahora-si-jqdr2awuqu2v3qgtm5tt2b.streamlit.app/"
    },
    {
        "numero": 3,
        "titulo": "Voz a texto multilingüe",
        "imagen": "traductor.jpg",
        "descripcion": "Aplicación que permite convertir voz en texto y trabajar con diferentes idiomas.",
        "texto_enlace": "Voz a texto",
        "url": "https://cualquiercosa-9vujzvkt47ulpaigzy82em.streamlit.app/"
    },
    {
        "numero": 4,
        "titulo": "Imagen a texto (OCR) y análisis de vocales",
        "imagen": "ocr.jpg",
        "descripcion": "Aplicación que permite extraer texto de imágenes mediante OCR y realizar análisis de vocales.",
        "texto_enlace": "OCR",
        "url": "https://aplicacion-75drrvtjhfwfrvhehhudhk.streamlit.app/"
    },
    {
        "numero": 5,
        "titulo": "Evaluación automática TF",
        "imagen": "analis.jpg",
        "descripcion": "Aplicación para realizar procesos de evaluación automática utilizando Inteligencia Artificial.",
        "texto_enlace": "Evaluación",
        "url": "https://tdfesp-admzi2whggzdysyv6hrrzw.streamlit.app/"
    },
    {
        "numero": 6,
        "titulo": "Reconocimiento de emociones",
        "imagen": "reconocmiento.jpg",
        "descripcion": "Aplicación que permite reconocer y analizar emociones mediante Inteligencia Artificial.",
        "texto_enlace": "Emociones",
        "url": "https://sentimenta-8iy82nmkh7fnyggx7cecu5.streamlit.app/"
    },
    {
        "numero": 7,
        "titulo": "Detección de objetos en imágenes",
        "imagen": "recobj.jpg",
        "descripcion": "Aplicación que permite detectar diferentes objetos dentro de imágenes mediante Inteligencia Artificial.",
        "texto_enlace": "Detección de objetos",
        "url": "https://yolov5-nemrh4dhsxvkjiv4bakkhb.streamlit.app/"
    },
    {
        "numero": 8,
        "titulo": "Nube de palabras",
        "imagen": "nube.jpg",
        "descripcion": "Aplicación que permite generar nubes de palabras a partir de textos y datos.",
        "texto_enlace": "Nube de palabras",
        "url": "https://wordcloud-2urj9yggquvij7xmnmsqtv.streamlit.app/"
    },
    {
        "numero": 9,
        "titulo": "Teachable Machine",
        "imagen": "TM.jpg",
        "descripcion": "Aplicación para entrenar modelos de Inteligencia Artificial y realizar predicciones.",
        "texto_enlace": "Teachable Machine",
        "url": "https://tm-detection-npqnkslgj6ps87sj9fvtre.streamlit.app/"
    },
    {
        "numero": 10,
        "titulo": "TM entrenada",
        "imagen": "TM.jpg",
        "descripcion": "Aplicación basada en un modelo de Teachable Machine previamente entrenado para realizar predicciones.",
        "texto_enlace": "TM entrenada",
        "url": "https://tm-detection-npqnkslgj6ps87sj9fvtre.streamlit.app/"
    },

    # NUEVAS APLICACIONES

    {
        "numero": 11,
        "titulo": "Análisis de PDF",
        "imagen": "PDF.jpg",
        "descripcion": "Aplicación que permite analizar documentos PDF y consultar su contenido mediante Inteligencia Artificial.",
        "texto_enlace": "Analizar PDF",
        "url": "https://chatpdf-p8dreedbl7mfyb5stkrtnn.streamlit.app/"
    },
    {
        "numero": 12,
        "titulo": "Reconocimiento de imágenes",
        "imagen": "recogimg.jpg",
        "descripcion": "Aplicación de visión artificial para reconocer y analizar imágenes.",
        "texto_enlace": "Reconocer imágenes",
        "url": "https://visionapp-dp5s9n48czuerqc3nvfqm9.streamlit.app/"
    },
    {
        "numero": 13,
        "titulo": "Tablero inteligente",
        "imagen": "tablero.jpg",
        "descripcion": "Tablero inteligente para interactuar con trazos y dibujos.",
        "texto_enlace": "Abrir tablero",
        "url": "https://drawrecog-jmupgqvg3stu5w4cxp9edw.streamlit.app/"
    },
    {
        "numero": 14,
        "titulo": "Tablero personalizado",
        "imagen": "tableropers.jpg",
        "descripcion": "Tablero interactivo personalizado para realizar actividades y explorar diferentes funciones.",
        "texto_enlace": "Abrir tablero",
        "url": "https://tableroperzonalizado-evetxxy6wgjcysafhgygb7.streamlit.app/"
    },
    {
        "numero": 15,
        "titulo": "Detección de dígitos a mano",
        "imagen": "detecnum.jpg",
        "descripcion": "Reconoce dígitos escritos a mano mediante un modelo de aprendizaje automático.",
        "texto_enlace": "Detectar dígitos",
        "url": "https://mnistpred-hrccjfx4k2uhhhk7gcyz8u.streamlit.app/"
    },
    {
        "numero": 16,
        "titulo": "Reconocimiento de dibujos",
        "imagen": "recogdibuj.jpg",
        "descripcion": "Aplicación para reconocer dibujos y explorar técnicas de reconocimiento visual.",
        "texto_enlace": "Reconocer dibujos",
        "url": "https://drawrecog-5nug9hv5mbhqxqnl7keuw6.streamlit.app/"
    },
    {
        "numero": 17,
        "titulo": "Control por voz",
        "imagen": "controlvoz.jpg",
        "descripcion": "Aplicación que permite interactuar mediante comandos de voz.",
        "texto_enlace": "Control por voz",
        "url": "https://ctrlvoice-2n9fh65uoadnjyatelq4br.streamlit.app/"
    },
    {
        "numero": 18,
        "titulo": "Lector del sensor MQTT",
        "imagen": "lectorsensor.jpg",
        "descripcion": "Consulta información recibida desde sensores mediante comunicación MQTT.",
        "texto_enlace": "Leer sensor MQTT",
        "url": "https://recepmqtt-igzow4v3hzzukrud6nuxh2.streamlit.app/"
    },
    {
        "numero": 19,
        "titulo": "Control MQTT de la puerta",
        "imagen": "controlmqttpuer.jpg",
        "descripcion": "Aplicación para controlar una puerta a través de comunicación MQTT.",
        "texto_enlace": "Controlar puerta",
        "url": "https://sendcmqtt-mcsjjva9qirwj2qmupvpmz.streamlit.app/"
    },
    {
        "numero": 20,
        "titulo": "Control por voz y MQTT",
        "imagen": "controlvoz.jpg",
        "descripcion": "Combina comandos de voz y comunicación MQTT para interactuar con dispositivos.",
        "texto_enlace": "Abrir aplicación",
        "url": "https://clas14dossi-ydncff72jne6pzhstabi2s.streamlit.app/Control_por_voz"
    },
    {
        "numero": 21,
        "titulo": "TM y YOLO",
        "imagen": "tmyolo.jpg",
        "descripcion": "Aplicación que integra herramientas de reconocimiento y detección de objetos.",
        "texto_enlace": "TM y YOLO",
        "url": "https://clase14si-v5lfqi9eefjxnbgrmzyg3q.streamlit.app/Teachable_Machine"
    },
    {
        "numero": 22,
        "titulo": "Cerradura por gestos",
        "imagen": "cerraduragest.jpg",
        "descripcion": "Aplicación de cerradura que utiliza gestos como mecanismo de interacción.",
        "texto_enlace": "Cerradura por gestos",
        "url": "https://cerraduragestos-kdp3zunq4neexhrtkjgl3t.streamlit.app/"
    },
]


# ============================================================
# MOSTRAR APLICACIONES EN TRES COLUMNAS
# ============================================================

col1, col2, col3 = st.columns(3)
columnas = [col1, col2, col3]

for indice, aplicacion in enumerate(aplicaciones):
    with columnas[indice % 3]:
        mostrar_tarjeta(
            aplicacion["numero"],
            aplicacion["titulo"],
            aplicacion["imagen"],
            aplicacion["descripcion"],
            aplicacion["texto_enlace"],
            aplicacion["url"]
        )


# ============================================================
# PIE DE PÁGINA
# ============================================================

st.markdown(
    '<div class="footer">'
    '🤖 Aplicaciones de Inteligencia Artificial'
    '<br>'
    'Proyecto educativo · Streamlit'
    '</div>',
    unsafe_allow_html=True
)
