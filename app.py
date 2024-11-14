# Importat librerías
import streamlit as st
from form_validate import validate_form



# Cargar variables de entorno
ELECTIVO_1 = st.secrets["ELECTIVO_1"]
ELECTIVO_2 = st.secrets["ELECTIVO_2"]
ELECTIVO_3 = st.secrets["ELECTIVO_3"]
CURSOS = st.secrets["CURSOS"]
ELECTIVOS_FG = st.secrets["ELECTIVOS_FG"]

# Título
st.title("Formulario de Inscripción de Electivos - 2024")
st.text("Recuerda que debes seguir las reglas para inscribirte correctamente.")

# Identificación del estudiante
with st.form(key="form"):

    # --- Sección de identificación del estudiante ---
    st.header("Identificación del estudiante")

    # Nombre
    name = st.text_input("Ingresa tu nombre completo", placeholder="Nombre Completo")
    st.caption("Ejemplo: Francisca Alejandra Pérez Ortiz")

    # RUN
    run = st.text_input("Ingresa tu RUN", placeholder="12345678-k")
    st.caption(
        "Debes ingresar tu run sin puntos, con guión y dígito verificador. Ej.: 11222333-X"
    )

    # Email
    email = st.text_input(
        "Ingresa tu correo institucional",
        placeholder="nombre.apellido@estudiantes.colegiotgs.cl",
    )
    st.caption("Ejemplo: francisca.perez@estudiantes.colegiotgs.cl")

    # Curso
    curso = st.radio("Selecciona tu curso", CURSOS, index=None)

    # --- Sección de inscripción Formación Diferenciada ---
    st.divider()

    # Seleccionar los electivos de formación diferenciada
    st.header("Electivos de Formación Diferenciada")

    # Electivo 1
    electivo_1 = st.radio(
        "Selecciona el Electivo 1",
        ELECTIVO_1,
        index=None,
    )

    # Electivo 2
    electivo_2 = st.radio(
        "Selecciona el Electivo 2",
        ELECTIVO_2,
        index=None,
    )

    # Electivo 3
    electivo_3 = st.radio(
        "Selecciona el Electivo 3",
        ELECTIVO_3,
        index=None,
    )

    st.divider()

    # Electivos de Formación General
    st.header("Electivos de Formación General")

    electivo_fg = st.radio(
        "Selecciona el Electivo de Formación General",
        ELECTIVOS_FG,
        index=None,
    )
    submit_button = st.form_submit_button(label="Enviar")

# Botón para enviar el formulario
if submit_button:
    if validate_form(
        name, run, email, curso, electivo_1, electivo_2, electivo_3, electivo_fg
    ):
        st.success("Tu inscripción ha sido exitosa. Puedes tomar una captura para tener un respaldo de tu inscripción o esperar a tu inscripción en papel.")
