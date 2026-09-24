import streamlit as st
from PIL import Image

st.title("Aplicaciones de Inteligencia Artificial.")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")

    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )

    st.write(parrafo)


# ============================================================
# ENLACE GENERAL
# ============================================================

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.subheader(
    "En el siguiente enlace puedes encontrar páginas y ejercicios prácticos"
)

st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")


# ============================================================
# ESTILO
# ============================================================

st.markdown(
    """
    <style>
    .app-card {
        height: 430px;
        margin-bottom: 25px;
    }

    .app-title {
        height: 65px;
    }

    .app-image {
        height: 210px;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .app-description {
        height: 80px;
    }
    </style>
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

    # 1. INTRODUCCIÓN
    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="app-title"><h3>Introducción</h3></div>',
        unsafe_allow_html=True
    )

    image = Image.open("inttro.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="app-description">'
        'En esta aplicación se presenta una introducción a las '
        'aplicaciones de la Inteligencia Artificial.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://estesi-z29ropifyfvwhuted9mfsb.streamlit.app/"
    st.write(f"Introducción: [Enlace]({url})")

    st.markdown('</div>', unsafe_allow_html=True)


    # 2. TEXTO A VOZ
    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="app-title"><h3>Conversión de texto a voz</h3></div>',
        unsafe_allow_html=True
    )

    image = Image.open("texttospeech.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="app-description">'
        'Aplicación que permite convertir texto escrito '
        'en voz mediante Inteligencia Artificial.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://ahora-si-jqdr2awuqu2v3qgtm5tt2b.streamlit.app/"
    st.write(f"Texto a voz: [Enlace]({url})")

    st.markdown('</div>', unsafe_allow_html=True)


    # 3. VOZ A TEXTO
    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="app-title"><h3>Voz a texto multilingüe</h3></div>',
        unsafe_allow_html=True
    )

    image = Image.open("traductor.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="app-description">'
        'Aplicación que permite convertir voz en texto '
        'y trabajar con diferentes idiomas.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://cualquiercosa-9vujzvkt47ulpaigzy82em.streamlit.app/"
    st.write(f"Voz a texto: [Enlace]({url})")

    st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# COLUMNA 2
# ============================================================

with col2:

    # 4. OCR
    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="app-title"><h3>Imagen a texto (OCR)</h3></div>',
        unsafe_allow_html=True
    )

    image = Image.open("ocr.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="app-description">'
        'Aplicación que permite extraer texto de imágenes '
        'mediante OCR y realizar análisis de vocales.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://aplicacion-75drrvtjhfwfrvhehhudhk.streamlit.app/"
    st.write(f"OCR: [Enlace]({url})")

    st.markdown('</div>', unsafe_allow_html=True)


    # 5. EVALUACIÓN
    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="app-title"><h3>Evaluación automática TF</h3></div>',
        unsafe_allow_html=True
    )

    image = Image.open("analis.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="app-description">'
        'Aplicación para realizar procesos de evaluación '
        'automática utilizando Inteligencia Artificial.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://tdfesp-admzi2whggzdysyv6hrrzw.streamlit.app/"
    st.write(f"Evaluación: [Enlace]({url})")

    st.markdown('</div>', unsafe_allow_html=True)


    # 6. EMOCIONES
    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="app-title"><h3>Reconocimiento de emociones</h3></div>',
        unsafe_allow_html=True
    )

    image = Image.open("reconocmiento.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="app-description">'
        'Aplicación que permite reconocer y analizar '
        'emociones mediante Inteligencia Artificial.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://sentimenta-8iy82nmkh7fnyggx7cecu5.streamlit.app/"
    st.write(f"Emociones: [Enlace]({url})")

    st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# COLUMNA 3
# ============================================================

with col3:

    # 7. DETECCIÓN DE OBJETOS
    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="app-title"><h3>Detección de objetos en imágenes</h3></div>',
        unsafe_allow_html=True
    )

    image = Image.open("recobj.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="app-description">'
        'Aplicación que permite detectar diferentes objetos '
        'dentro de imágenes mediante Inteligencia Artificial.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://yolov5-nemrh4dhsxvkjiv4bakkhb.streamlit.app/"
    st.write(f"Detección de objetos: [Enlace]({url})")

    st.markdown('</div>', unsafe_allow_html=True)


    # 8. NUBE DE PALABRAS
    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="app-title"><h3>Nube de palabras</h3></div>',
        unsafe_allow_html=True
    )

    image = Image.open("nube.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="app-description">'
        'Aplicación que permite generar nubes de palabras '
        'a partir de textos y datos.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://wordcloud-2urj9yggquvij7xmnmsqtv.streamlit.app/"
    st.write(f"Nube de palabras: [Enlace]({url})")

    st.markdown('</div>', unsafe_allow_html=True)


    # 9. TEACHABLE MACHINE
    st.markdown('<div class="app-card">', unsafe_allow_html=True)

    st.markdown(
        '<div class="app-title"><h3>Teachable Machine</h3></div>',
        unsafe_allow_html=True
    )

    image = Image.open("TM.jpg")
    st.image(image, width=200)

    st.markdown(
        '<div class="app-description">'
        'Aplicación para entrenar modelos de Inteligencia Artificial '
        'y utilizarlos posteriormente para realizar predicciones.'
        '</div>',
        unsafe_allow_html=True
    )

    url = "https://tm-detection-npqnkslgj6ps87sj9fvtre.streamlit.app/"
    st.write(f"Teachable Machine: [Enlace]({url})")

    st.markdown('</div>', unsafe_allow_html=True)
