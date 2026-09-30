import streamlit as st
from PIL import Image, ImageOps

# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Aplicaciones de Inteligencia Artificial",
    layout="wide"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

    /* Título principal */
    h1 {
        margin-bottom: 10px;
    }

    /* Espacio entre columnas */
    [data-testid="column"] {
        padding-left: 15px;
        padding-right: 15px;
    }

    /* Tarjetas */
    .tarjeta {
        padding: 5px;
        margin-bottom: 35px;
    }

    /* Título de cada aplicación */
    .titulo-tarjeta {
        height: 90px;
        display: flex;
        align-items: flex-start;
    }

    .titulo-tarjeta h3 {
        margin-top: 0;
        font-size: 25px;
        line-height: 1.15;
    }

    /* Imagen */
    .imagen-tarjeta {
        width: 100%;
        height: 170px;
        object-fit: cover;
        border-radius: 10px;
        display: block;
    }

    /* Descripción */
    .descripcion-tarjeta {
        min-height: 105px;
        font-size: 17px;
        line-height: 1.6;
        padding-top: 15px;
    }

    /* Enlace */
    .enlace-tarjeta {
        height: 40px;
        font-size: 16px;
    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# FUNCIÓN PARA MOSTRAR TARJETAS
# ============================================================

def mostrar_tarjeta(titulo, imagen, descripcion, texto_enlace, url):

    # Título con altura fija
    st.markdown(
        f"""
        <div class="titulo-tarjeta">
            <h3>{titulo}</h3>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Abrir y adaptar imagen a tamaño uniforme
    img = Image.open(imagen)

    # Todas las imágenes tendrán exactamente la misma proporción
    img = ImageOps.fit(
        img,
        (600, 300),
        method=Image.Resampling.LANCZOS
    )

    st.image(
        img,
        width="stretch"
    )

    # Descripción con altura mínima
    st.markdown(
        f"""
        <div class="descripcion-tarjeta">
            {descripcion}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Enlace
    st.markdown(
        f"""
        <div class="enlace-tarjeta">
            {texto_enlace}: <a href="{url}" target="_blank">Enlace</a>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# TÍTULO
# ============================================================

st.title("Aplicaciones de Inteligencia Artificial.")


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.subheader("Aplicaciones con Inteligencia Artificial.")

    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones "
        "con el uso de datos, automatizar tareas rutinarias y proporcionar "
        "análisis avanzados en tiempo real, lo que resulta en una mayor "
        "eficiencia y precisión en diversos campos."
    )

    st.write(parrafo)


# ============================================================
# ENLACE GENERAL
# ============================================================

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.subheader(
    "En el siguiente enlace puedes encontrar páginas y ejercicios prácticos"
)

st.write(
    f"Enlace para páginas y ejercicios: [Enlace]({url_ia})"
)


# ============================================================
# COLUMNAS
# ============================================================

col1, col2, col3 = st.columns(3)


# ============================================================
# COLUMNA 1
# ============================================================

with col1:

    # 1. INTRODUCCIÓN
    mostrar_tarjeta(
        "Introducción",
        "inttro.jpg",
        "En esta aplicación se presenta una introducción "
        "a las aplicaciones de la Inteligencia Artificial.",
        "Introducción",
        "https://estesi-z29ropifyfvwhuted9mfsb.streamlit.app/"
    )

    # 2. TEXTO A VOZ
    mostrar_tarjeta(
        "Conversión de texto a voz",
        "texttospeech.jpg",
        "Aplicación que permite convertir texto escrito "
        "en voz mediante Inteligencia Artificial.",
        "Texto a voz",
        "https://ahora-si-jqdr2awuqu2v3qgtm5tt2b.streamlit.app/"
    )

    # 3. VOZ A TEXTO
    mostrar_tarjeta(
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

    # 4. OCR
    mostrar_tarjeta(
        "Imagen a texto (OCR) y análisis de vocales",
        "ocr.jpg",
        "Aplicación que permite extraer texto de imágenes "
        "mediante reconocimiento óptico de caracteres (OCR) "
        "y realizar análisis de vocales.",
        "OCR",
        "https://aplicacion-75drrvtjhfwfrvhehhudhk.streamlit.app/"
    )

    # 5. EVALUACIÓN
    mostrar_tarjeta(
        "Evaluación automática TF",
        "analis.jpg",
        "Aplicación para realizar procesos de evaluación "
        "automática utilizando Inteligencia Artificial.",
        "Evaluación",
        "https://tdfesp-admzi2whggzdysyv6hrrzw.streamlit.app/"
    )

    # 6. EMOCIONES
    mostrar_tarjeta(
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

    # 7. DETECCIÓN DE OBJETOS
    mostrar_tarjeta(
        "Detección de objetos en imágenes",
        "recobj.jpg",
        "Aplicación que permite detectar diferentes objetos "
        "dentro de imágenes mediante Inteligencia Artificial.",
        "Detección de objetos",
        "https://yolov5-nemrh4dhsxvkjiv4bakkhb.streamlit.app/"
    )

    # 8. NUBE DE PALABRAS
    mostrar_tarjeta(
        "Nube de palabras",
        "nube.jpg",
        "Aplicación que permite generar nubes de palabras "
        "a partir de textos y datos.",
        "Nube de palabras",
        "https://wordcloud-2urj9yggquvij7xmnmsqtv.streamlit.app/"
    )

    # 9. TEACHABLE MACHINE
    mostrar_tarjeta(
        "Teachable Machine",
        "TM.jpg",
        "Aplicación para entrenar modelos de Inteligencia "
        "Artificial y utilizarlos posteriormente para "
        "realizar predicciones.",
        "Teachable Machine",
        "https://tm-detection-npqnkslgj6ps87sj9fvtre.streamlit.app/"
    )

