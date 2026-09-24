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


# Enlace general
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"

st.subheader(
    "En el siguiente enlace puedes encontrar páginas y ejercicios prácticos"
)

st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")


# ============================================================
# COLUMNAS
# ============================================================

col1, col2, col3 = st.columns(3)


# ============================================================
# COLUMNA 1
# ============================================================

with col1:

    # --------------------------------------------------------
    # 1. INTRODUCCIÓN
    # --------------------------------------------------------

    st.subheader("Introducción")

    # >>> AGREGA AQUÍ LA IMAGEN DE INTRODUCCIÓN <<<
    image = Image.open("IMAGEN_INTRODUCCION.png")
    st.image(image, width=200)

    st.write(
        "En esta aplicación se presenta una introducción a las "
        "aplicaciones de la Inteligencia Artificial."
    )

    url = "https://estesi-z29ropifyfvwhuted9mfsb.streamlit.app/"

    st.write(f"Introducción: [Enlace]({url})")


    # --------------------------------------------------------
    # 2. CONVERSIÓN DE TEXTO A VOZ
    # --------------------------------------------------------

    st.subheader("Conversión de texto a voz")

    # >>> AGREGA AQUÍ LA IMAGEN DE TEXTO A VOZ <<<
    image = Image.open("IMAGEN_TEXTO_VOZ.png")
    st.image(image, width=200)

    st.write(
        "Aplicación que permite convertir texto escrito "
        "en voz mediante Inteligencia Artificial."
    )

    url = "https://ahora-si-jqdr2awuqu2v3qgtm5tt2b.streamlit.app/"

    st.write(f"Texto a voz: [Enlace]({url})")


    # --------------------------------------------------------
    # 3. VOZ A TEXTO MULTILINGÜE
    # --------------------------------------------------------

    st.subheader("Voz a texto multilingüe")

    # >>> AGREGA AQUÍ LA IMAGEN DE VOZ A TEXTO <<<
    image = Image.open("IMAGEN_VOZ_TEXTO.png")
    st.image(image, width=200)

    st.write(
        "Aplicación que permite convertir voz en texto "
        "y trabajar con diferentes idiomas."
    )

    url = "https://cualquiercosa-9vujzvkt47ulpaigzy82em.streamlit.app/"

    st.write(f"Voz a texto: [Enlace]({url})")


# ============================================================
# COLUMNA 2
# ============================================================

with col2:

    # --------------------------------------------------------
    # 4. IMAGEN A TEXTO / OCR
    # --------------------------------------------------------

    st.subheader("Imagen a texto (OCR) y análisis de vocales")

    # >>> AGREGA AQUÍ LA IMAGEN DE OCR <<<
    image = Image.open("IMAGEN_OCR.png")
    st.image(image, width=200)

    st.write(
        "Aplicación que permite extraer texto de imágenes "
        "mediante reconocimiento óptico de caracteres (OCR) "
        "y realizar análisis de vocales."
    )

    url = "https://aplicacion-75drrvtjhfwfrvhehhudhk.streamlit.app/"

    st.write(f"OCR: [Enlace]({url})")


    # --------------------------------------------------------
    # 5. EVALUACIÓN AUTOMÁTICA TF
    # --------------------------------------------------------

    st.subheader("Evaluación automática TF")

    # >>> AGREGA AQUÍ LA IMAGEN DE EVALUACIÓN <<<
    image = Image.open("IMAGEN_EVALUACION.png")
    st.image(image, width=200)

    st.write(
        "Aplicación para realizar procesos de evaluación "
        "automática utilizando Inteligencia Artificial."
    )

    url = "https://tdfesp-admzi2whggzdysyv6hrrzw.streamlit.app/"

    st.write(f"Evaluación: [Enlace]({url})")


    # --------------------------------------------------------
    # 6. RECONOCIMIENTO DE EMOCIONES
    # --------------------------------------------------------

    st.subheader("Reconocimiento de emociones")

    # >>> AGREGA AQUÍ LA IMAGEN DE EMOCIONES <<<
    image = Image.open("IMAGEN_EMOCIONES.png")
    st.image(image, width=200)

    st.write(
        "Aplicación que permite reconocer y analizar "
        "emociones mediante Inteligencia Artificial."
    )

    url = "https://sentimenta-8iy82nmkh7fnyggx7cecu5.streamlit.app/"

    st.write(f"Emociones: [Enlace]({url})")


# ============================================================
# COLUMNA 3
# ============================================================

with col3:

    # --------------------------------------------------------
    # 7. DETECCIÓN DE OBJETOS
    # --------------------------------------------------------

    st.subheader("Detección de objetos en imágenes")

    # >>> AGREGA AQUÍ LA IMAGEN DE DETECCIÓN DE OBJETOS <<<
    image = Image.open("IMAGEN_OBJETOS.png")
    st.image(image, width=200)

    st.write(
        "Aplicación que permite detectar diferentes objetos "
        "dentro de imágenes mediante Inteligencia Artificial."
    )

    url = "https://yolov5-nemrh4dhsxvkjiv4bakkhb.streamlit.app/"

    st.write(f"Detección de objetos: [Enlace]({url})")


    # --------------------------------------------------------
    # 8. NUBE DE PALABRAS
    # --------------------------------------------------------

    st.subheader("Nube de palabras")

    # >>> AGREGA AQUÍ LA IMAGEN DE NUBE DE PALABRAS <<<
    image = Image.open("IMAGEN_NUBE_PALABRAS.png")
    st.image(image, width=200)

    st.write(
        "Aplicación que permite generar nubes de palabras "
        "a partir de textos y datos."
    )

    url = "https://wordcloud-2urj9yggquvij7xmnmsqtv.streamlit.app/"

    st.write(f"Nube de palabras: [Enlace]({url})")


    # --------------------------------------------------------
    # 9. TEACHABLE MACHINE
    # --------------------------------------------------------

    st.subheader("Teachable Machine")

    # >>> AGREGA AQUÍ LA IMAGEN DE TEACHABLE MACHINE <<<
    image = Image.open("IMAGEN_TEACHABLE_MACHINE.png")
    st.image(image, width=200)

    st.write(
        "Aplicación para entrenar modelos de Inteligencia Artificial "
        "y utilizarlos posteriormente para realizar predicciones."
    )

    url = "https://tm-detection-npqnkslgj6ps87sj9fvtre.streamlit.app/"

    st.write(f"Teachable Machine: [Enlace]({url})")

