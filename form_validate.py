import streamlit as st
import re
from control_form import verify_email, insert_user

# Definir la expresión regular para un RUN chileno
run_regex = r'^\d{7,8}-[\dKk]$'

# Compilar la expresión regular
pattern_run = re.compile(run_regex)


# Definir una función para validar el RUN chileno
def is_valid_run(run):
    return bool(pattern_run.fullmatch(run))

def validate_form(name, run, email, curso, electivo_1, electivo_2, electivo_3, electivo_fg):
    if run and not is_valid_run(run):
        st.error("RUN no válido")
    elif email and not verify_email(email):
        st.error("El email ingresado no es válido")
    else:
        if not name:
            st.error("Debes ingresar el nombre completo")
        elif not run:
            st.error("Debes ingresar el RUN")
        elif not email:
            st.error("Debes ingresar tu email")
        elif not curso:
            st.error("Debes seleccionar tu curso")
        elif not electivo_1:
            st.error("Debes seleccionar el electivo 1")
        elif not electivo_2:
            st.error("Debes seleccionar el electivo 2")
        elif not electivo_3:
            st.error("Debes seleccionar el electivo 3")
        elif not electivo_fg:
            st.error("Debes seleccionar el electivo de formación general")
        else:
            if insert_user(name, run, email, curso, electivo_1, electivo_2, electivo_3, electivo_fg):
                return True
            else:
                st.error("Error al enviar el formulario. Inteéntalo de nuevo.")