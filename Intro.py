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
# CSS PERSONALIZADO
# ============================================================

st.markdown("""
<style>

    /* ========================================================
       FONDO GENERAL
       ======================================================== */

    .stApp {
        background:
            radial-gradient(circle at top left, #312e81 0%, transparent 35%),
            radial-gradient(circle at top right, #0e7490 0%, transparent 30%),
            linear-gradient(135deg, #0f172a, #111827 55%, #1e1b4b);
        color: #f8fafc;
    }


    /* ========================================================
       SIDEBAR
       ======================================================== */

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
        color: white;
    }

    section[data-testid="stSidebar"] p {
        color: #cbd5e1;
        line-height: 1.7;
    }


    /* ========================================================
       TÍTULO PRINCIPAL
       ======================================================== */

    .titulo-principal {
        text-align: center;
        font-size: 3.2rem;
        font-weight: 900;
        margin-top: 10px;
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
        margin-bottom: 35px;
    }


    /* ========================================================
       CAJA DEL ENLACE GENERAL
       ======================================================== */

    .enlace-general {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 18px;

        padding: 20px 25px;
        margin: 20px 0 35px 0;

        box-shadow: 0 10px 35px rgba(0,0,0,0.25);

        backdrop-filter: blur(10px);
    }

    .enlace-general h3 {
        margin-top: 0;
        color: #f8fafc;
    }

    .enlace-general p {
        color: #cbd5e1;
    }


    /* ========================================================
       TARJETAS
       ======================================================== */

    .tarjeta {
        background: rgba(255,255,255,0.07);

        border: 1px solid rgba(255,255,255,0.12);

        border-radius: 20px;

        padding: 18px;

        margin-bottom: 35px;

        min-height: 430px;

        box-shadow:
            0 12px 30px rgba(0,0,0,0.30);

        backdrop-filter: blur(10px);

        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease,
            border-color 0.25s ease;
    }


    /* Efecto al pasar el mouse */

    .tarjeta:hover {
        transform: translateY(-7px);

        border-color: rgba(129,140,248,0.7);

        box-shadow:
            0 20px 45px rgba(0,0,0,0.45),
            0 0 25px rgba(99,102,241,0.15);
    }


    /* ========================================================
       NÚMERO DE APLICACIÓN
       ======================================================== */

    .numero {
        display: inline-block;

        background: linear-gradient(
            135deg,
            #38bdf8,
            #6366f1
        );

        color: white;

        font-size: 13px;
        font-weight: 700;

        padding: 5px 10px;

        border-radius: 20px;

        margin-bottom: 10px;
    }


    /* ========================================================
       TÍTULO DE TARJETA
       ======================================================== */

    .titulo-tarjeta {
        height: 75px;

        display: flex;
        align-items: flex-start;
    }

    .titulo-tarjeta h3 {
        margin: 0;

        color: #f8fafc;

        font-size: 22px;

        line-height: 1.2;

        font-weight: 750;
    }


    /* ========================================================
       IMÁGENES
       ======================================================== */

    .imagen-tarjeta {
        width: 100%;

        height: 180px;

        object-fit: cover;

        border-radius: 14px;

        display: block;

        border: 1px solid rgba(255,255,255,0.1);
    }


    /* ========================================================
       DESCRIPCIÓN
       ======================================================== */

    .descripcion-tarjeta {
        min-height: 105px;

        font-size: 15px;

        line-height: 1.6;

        padding-top: 15px;

        color: #cbd5e1;
    }


    /* ========================================================
       BOTÓN
       ======================================================== */

    .boton-enlace {
        display: block;

        text-align: center;

        padding: 11px 15px;

        border-radius: 12px;

        text-decoration: none;

        font-weight: 700;

        color: white !important;

        background: linear-gradient(
            135deg,
            #2563eb,
            #7c3aed
        );

        box-shadow:
            0 5px 15px rgba(37,99,235,0.25);

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .boton-enlace:hover {
        transform: scale(1.03);

        box-shadow:
            0 8px 22px rgba(124,58,237,0.4);

        text-decoration: none;
    }


    /* ========================================================
       SEPARADOR
       ======================================================== */

    hr {
        border-color: rgba(255,255,255,0.12);
    }


    /* ========================================================
       COLUMNAS
       ======================================================== */

    [data-testid="column"] {
        padding-left: 10px;
        padding-right: 10px;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

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

    st.markdown(
        f"""
        <div class="tarjeta">

            <div class="numero">
                Aplicación {numero}
            </div>

            <div class="titulo-tarjeta">
                <h3>{titulo}</h3>
            </div>

        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------
    # IMAGEN
    # --------------------------------------------------------

    img = Image.open(imagen)

    img = ImageOps.fit(
        img,
        (600, 300),
        method=Image.Resampling.LANCZOS
    )

    st.image(
        img,
        width="stretch"
    )

    # --------------------------------------------------------
    # DESCRIPCIÓN
    # --------------------------------------------------------

    st.markdown(
        f"""
            <div class="descripcion-tarjeta">
                {descripcion}
            </div>

            <a
                href="{url}"
                target="_blank"
                class="boton-enlace"
            >
                🚀 Abrir aplicación
            </a>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# ENCABEZADO
# ============================================================

st.markdown(
    """
    <div class="titulo-principal">
        🤖 Aplicaciones de Inteligencia Artificial
    </div>

    <div class="subtitulo-principal">
        Explora diferentes herramientas y aplicaciones
        desarrolladas con Inteligencia Artificial
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown("## 🤖 Inteligencia Artificial")

    st.markdown("---")

    st.markdown("### 📚 Sobre este proyecto")

    parrafo = (
        "La inteligencia artificial permite mejorar la toma "
        "de decisiones mediante el uso de datos, automatizar "
        "tareas rutinarias y proporcionar análisis avanzados "
        "en tiempo real."
    )

    st.write(parrafo)

    st.markdown("---")

    st.markdown("### 🧠 Aplicaciones disponibles")

    st.write("🎙️ Texto y voz")
    st.write("📝 Procesamiento de texto")
    st.write("👁️ Visión artificial")
    st.write("😊 Reconocimiento de emociones")
    st.write("🎯 Detección de objetos")
    st.write("☁️ Análisis de palabras")
    st.write("🤖 Machine Learning")


# ============================================================
# ENLACE GENERAL
# ============================================================

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.markdown(
    f"""
    <div class="enlace-general">

        <h3>📖 Recursos y ejercicios</h3>

        <p>
            En el siguiente enlace puedes encontrar páginas,
            recursos y ejercicios prácticos relacionados con
            las aplicaciones de Inteligencia Artificial.
        </p>

        <a
            href="{url_ia}"
            target="_blank"
            class="boton-enlace"
        >
            🌐 Ver recursos y ejercicios
        </a>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# COLUMNAS
# ============================================================

col1, col2, col3 = st.columns(3)


# ============================================================
# COLUMNA 1
# ============================================================

with col1:

    mostrar_tarjeta(
        1,
        "Introducción",
        "inttro.jpg",
        "En esta aplicación se presenta una introducción "
        "a las aplicaciones de la Inteligencia Artificial.",
        "Introducción",
        "https://estesi-z29ropifyfvwhuted9mfsb.streamlit.app/"
    )

    mostrar_tarjeta(
        2,
        "Conversión de texto a voz",
        "texttospeech.jpg",
        "Aplicación que permite convertir texto escrito "
        "en voz mediante Inteligencia Artificial.",
        "Texto a voz",
        "https://ahora-si-jqdr2awuqu2v3qgtm5tt2b.streamlit.app/"
    )

    mostrar_tarjeta(
        3,
        "Voz a texto multilingüe",
        "traductor.jpg",
        "Aplicación que permite convertir voz en texto "
        "y trabajar con diferentes idiomas.",
        "Voz a texto",
        "https://cualquiercosa-9vujzvkt47ulpaigzy82em.streamlit.app/"
    )


# ============================================================
# COLUMNA 2
# ============================================================

with col2:

    mostrar_tarjeta(
        4,
        "Imagen a texto (OCR) y análisis de vocales",
        "ocr.jpg",
        "Aplicación que permite extraer texto de imágenes "
        "mediante reconocimiento óptico de caracteres (OCR) "
        "y realizar análisis de vocales.",
        "OCR",
        "https://aplicacion-75drrvtjhfwfrvhehhudhk.streamlit.app/"
    )

    mostrar_tarjeta(
        5,
        "Evaluación automática TF",
        "analis.jpg",
        "Aplicación para realizar procesos de evaluación "
        "automática utilizando Inteligencia Artificial.",
        "Evaluación",
        "https://tdfesp-admzi2whggzdysyv6hrrzw.streamlit.app/"
    )

    mostrar_tarjeta(
        6,
        "Reconocimiento de emociones",
        "reconocmiento.jpg",
        "Aplicación que permite reconocer y analizar "
        "emociones mediante Inteligencia Artificial.",
        "Emociones",
        "https://sentimenta-8iy82nmkh7fnyggx7cecu5.streamlit.app/"
    )


# ============================================================
# COLUMNA 3
# ============================================================

with col3:

    mostrar_tarjeta(
        7,
        "Detección de objetos en imágenes",
        "recobj.jpg",
        "Aplicación que permite detectar diferentes objetos "
        "dentro de imágenes mediante Inteligencia Artificial.",
        "Detección de objetos",
        "https://yolov5-nemrh4dhsxvkjiv4bakkhb.streamlit.app/"
    )

    mostrar_tarjeta(
        8,
        "Nube de palabras",
        "nube.jpg",
        "Aplicación que permite generar nubes de palabras "
        "a partir de textos y datos.",
        "Nube de palabras",
        "https://wordcloud-2urj9yggquvij7xmnmsqtv.streamlit.app/"
    )

    mostrar_tarjeta(
        9,
        "Teachable Machine",
        "TM.jpg",
        "Aplicación para entrenar modelos de Inteligencia "
        "Artificial y utilizarlos posteriormente para "
        "realizar predicciones.",
        "Teachable Machine",
        "https://tm-detection-npqnkslgj6ps87sj9fvtre.streamlit.app/"
    )

    mostrar_tarjeta(
        10,
        "TM entrenada",
        "TM.jpg",
        "Aplicación basada en un modelo de Teachable Machine "
        "previamente entrenado para realizar predicciones "
        "mediante Inteligencia Artificial.",
        "TM entrenada",
        "https://tm-detection-npqnkslgj6ps87sj9fvtre.streamlit.app/"
    )


# ============================================================
# PIE DE PÁGINA
# ============================================================

st.markdown(
    """
    <div class="footer">
        🤖 Aplicaciones de Inteligencia Artificial
        <br>
        Proyecto educativo · Streamlit
    </div>
    """,
    unsafe_allow_html=True
)

