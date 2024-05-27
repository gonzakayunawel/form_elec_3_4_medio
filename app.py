import streamlit as st
from form_validate import validate_form

st.title("Formulario de Inscripción de Electivos - 2024")
st.text("Recuerda que debes seguir las reglas para inscribirte correctamente.")

with st.form(key="form"):
    st.header("Identificación del estudiante")

    name = st.text_input("Ingresa tu nombre completo", value="Nombre Completo")
    st.caption("Ejemplo: Francisca Alejandra Pérez Ortiz")
    run = st.text_input("Ingresa tu RUN", value="12345678-k")
    st.caption("Debes ingresar el RUN de tu curso. Ej.: XX.XXX.XXX-X")

    email = st.text_input(
        "Ingresa tu email",
        value="nombre.apellido@estudiantes.colegiotgs.cl",
    )
    st.caption('Si tu correo es apellido.nombre también es válido')
    curso = st.radio("Selecciona tu curso", ["III GREEN", "III BLUE"])

    st.divider()

    st.header("Electivos de Elección Formación Diferenciada")

    electivo_1 = st.radio(
        "Selecciona el Electivo 1",
        [
            "Área A: Comprensión Histórica del Presente",
            "Área B: Límites, Derivadas e Integrales",
            "Área C: Interpretación Musical",
        ],
    )

    electivo_2 = st.radio(
        "Selecciona el Electivo 2",
        [
            "Área A: Taller de literatura",
            "Área B: Biología celular y molecular",
            "Área B: Pensamiento computacional y programación",
            "Área C: Artes visuales, audiovisuales y multimediales"
        ],
    )

    electivo_3 = st.radio(
        "Selecciona el Electivo 3",
        [
            "Área A: Lectura y escritura especializada",
            "Área B: Química",
            "Área C: Ciencias del ejercicio físico y deportivo"
        ],
    )

    st.divider()

    st.header("Electivos de Formación General")

    electivo_fg = st.radio(
        "Selecciona el Electivo de Formación General",
        [
            "Historia, Geografía y Cs. Sociales",
            "Artes Visuales"
        ],
    )
    submit_button = st.form_submit_button(label='Enviar')

if submit_button:
    if validate_form(name, run, email, curso, electivo_1, electivo_2, electivo_3, electivo_fg):
        st.success("Gracias por enviar el formulario")
