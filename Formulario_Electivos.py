# Importat librerías
import streamlit as st
from form_validate import validate_form
from control_form import verify_email

# Título
st.title("Formulario de Inscripción de Electivos - 2024")
st.text("Recuerda que debes seguir las reglas para inscribirte correctamente.")

# Identificación del estudiante
with st.form(key="form"):
    st.header("Identificación del estudiante")
    # Nombre
    name = st.text_input("Ingresa tu nombre completo", placeholder="Nombre Completo")
    st.caption("Ejemplo: Francisca Alejandra Pérez Ortiz")
    # RUN
    run = st.text_input("Ingresa tu RUN", placeholder="12345678-k")
    st.caption(
        "Debes ingresar tu run sin puntos y con dígito verificador. Ej.: 11222333-X"
    )
    # Email
    email = st.text_input(
        "Ingresa tu correo institucional",
        placeholder="nombre.apellido@estudiantes.colegiotgs.cl",
    )
    st.caption("Ejemplo: francisca.perez@estudiantes.colegiotgs.cl")
    # Curso
    listado_cursos = ["III GREEN", "III BLUE"]
    curso = st.radio("Selecciona tu curso", listado_cursos, index=None)

    st.divider()

    # Seleccionar los electivos de formación diferenciada
    st.header("Electivos de Formación Diferenciada")

    # Electivo 1

    listado_electivos_1 = [
        "Área A: Comprensión Histórica del Presente",
        "Área B: Límites, Derivadas e Integrales",
        "Área C: Interpretación Musical",
    ]

    electivo_1 = st.radio(
        "Selecciona el Electivo 1",
        listado_electivos_1,
        index=None,
    )

    # Electivo 2

    listado_electivos_2 = [
        "Área A: Taller de literatura",
        "Área B: Biología celular y molecular",
        "Área B: Pensamiento computacional y programación",
        "Área C: Artes visuales, audiovisuales y multimediales",
    ]
    electivo_2 = st.radio(
        "Selecciona el Electivo 2",
        listado_electivos_2,
        index=None,
    )

    # Electivo 3

    listado_electivos_3 = [
        "Área A: Lectura y escritura especializada",
        "Área B: Química",
        "Área C: Ciencias del ejercicio físico y deportivo",
    ]
    electivo_3 = st.radio(
        "Selecciona el Electivo 3",
        listado_electivos_3,
        index=None,
    )

    st.divider()

    # Electivos de Formación General
    st.header("Electivos de Formación General")

    listado_electivos_fg = [
        "Historia, Geografía y Cs. Sociales",
        "Artes Visuales",
    ]
    electivo_fg = st.radio(
        "Selecciona el Electivo de Formación General",
        listado_electivos_fg,
        index=None,
    )
    submit_button = st.form_submit_button(label="Enviar")

# Botón para enviar el formulario
if submit_button:
    if validate_form(
        name, run, email, curso, electivo_1, electivo_2, electivo_3, electivo_fg
    ):
        st.success("Gracias por enviar el formulario")
