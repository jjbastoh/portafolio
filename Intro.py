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
# CSS
# ============================================================

st.markdown("""
<style>

    /* ========================================================
       FONDO
       ======================================================== */

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
        color: white !important;
    }

    section[data-testid="stSidebar"] p {
        color: #cbd5e1 !important;
        line-height: 1.7;
    }


    /* ========================================================
       TÍTULO
       ======================================================== */

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


    /* ========================================================
       CONTENEDORES DE LAS TARJETAS
       ======================================================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(255,255,255,0.12);
        border-radius: 20px;
        padding: 10px;

        box-shadow:
            0 12px 30px rgba(0,0,0,0.30);

        margin-bottom: 25px;
    }


    /* ========================================================
       TÍTULOS
       ======================================================== */

    .titulo-tarjeta {
        color: #f8fafc !important;
        font-size: 21px !important;
        font-weight: 750 !important;
        line-height: 1.25;
        min-height: 55px;
    }


    /* ========================================================
       NÚMERO
       ======================================================== */

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


    /* ========================================================
       DESCRIPCIÓN
       ======================================================== */

    .descripcion {
        color: #cbd5e1 !important;

        font-size: 15px;

        line-height: 1.6;

        min-height: 95px;

        padding-top: 8px;
    }


    /* ========================================================
       BOTONES
       ======================================================== */

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


    /* ========================================================
       IMÁGENES
       ======================================================== */

    [data-testid="stImage"] img {
        border-radius: 14px;
        border: 1px solid rgba(255,255,255,0.1);
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
# FUNCIÓN PARA MOSTRAR TARJETA
# ============================================================

def mostrar_tarjeta(
    numero,
    titulo,
    imagen,
    descripcion,
    texto_enlace,
    url
):

    # Crear tarjeta
    with st.container(border=True):

        # Número
        st.markdown(
            f'<div class="numero">Aplicación {numero}</div>',
            unsafe_allow_html=True
        )

        # Título
        st.markdown(
            f'<div class="titulo-tarjeta">{titulo}</div>',
            unsafe_allow_html=True
        )

        # Imagen
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

        except Exception as e:

            st.warning(
                f"No se pudo cargar la imagen: {imagen}"
            )

        # Descripción
        st.markdown(
            f'<div class="descripcion">{descripcion}</div>',
            unsafe_allow_html=True
        )

        # Botón
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
        "mediante reconocimiento óptico de caracteres "
        "(OCR) y realizar análisis de vocales.",
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
    '<div class="footer">'
    '🤖 Aplicaciones de Inteligencia Artificial'
    '<br>'
    'Proyecto educativo · Streamlit'
    '</div>',
    unsafe_allow_html=True
)

