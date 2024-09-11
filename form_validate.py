import streamlit as st
import re, sqlite3
from control_form import verify_email, insert_user_record

# Definir la expresión regular para un RUN chileno
run_regex = r"^\d{7,8}-[\dKk]$"

# Compilar la expresión regular
pattern_run = re.compile(run_regex)


# Definir una función para validar el RUN chileno
def is_valid_run(run):
    return bool(pattern_run.fullmatch(run))


# Definir una función para validar que los electivos no sean los 3 de la misma área


def validate_electivos(electivo_1: str, electivo_2: str, electivo_3: str):
    if electivo_1[:6] == electivo_2[:6] == electivo_3[:6]:
        return False
    else:
        return True


# Definir una función para validar si el electivo tiene cupo

def validate_elective_availability(
    electivo_elegido: str, electivo: str, availavity: int
):
    conn = sqlite3.connect("form_app.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            f"SELECT COUNT({electivo}) FROM users_register WHERE {electivo} = ?",
            (electivo_elegido,),
        )
        result = cursor.fetchone()
        if result[0] >= availavity:
            return False
        else:
            return True
    except Exception as e:
        raise e
    finally:
        conn.close()


cupos_electivos = 5


def validate_form(
    name, run, email, curso, electivo_1, electivo_2, electivo_3, electivo_fg
):
    if run and not is_valid_run(run):  # verif icar si el RUN es válido
        st.error("RUN no válido")
    elif email and not verify_email(
        email
    ):  # verificar si el email es válido y si existe en la base de datos
        st.error(
            "El email ingresado no es válido o no es un email habilitado para inscribirse"
        )
    else:
        if not name:
            st.error(
                "Debes ingresar el nombre completo"
            )  # verificar si el nombre ha sio ingresado
        elif not run:
            st.error("Debes ingresar el RUN")  # verificar si el RUN ha sido ingresado
        elif not email:
            st.error(
                "Debes ingresar tu email"
            )  # verificar si el email ha sido ingresado
        elif not curso:
            st.error(
                "Debes seleccionar tu curso"
            )  # verificar si el curso ha sido seleccionado
        elif not electivo_1:
            st.error(
                "Debes seleccionar el electivo 1"
            )  # verificar si el electivo 1 ha sido seleccionado
        elif not electivo_2:
            st.error(
                "Debes seleccionar el electivo 2"
            )  # verificar si el electivo 2 ha sido seleccionado
        elif not electivo_3:
            st.error(
                "Debes seleccionar el electivo 3"
            )  # verificar si el electivo 3 ha sido seleccionado
        elif not electivo_fg:
            st.error(
                "Debes seleccionar el electivo de formación general"
            )  # verificar si el electivo FG ha sido seleccionado
        else:
            if verify_email(email, table="users_register"):
                st.error(
                    "El email ya está en uso"
                )  # verificar si el email ya está en la base de datos de inscripciones
            elif not validate_electivos(electivo_1, electivo_2, electivo_3):
                st.error(
                    "Los electivos no pueden ser los 3 de la misma área"
                )  # verificar si los electivos no son los 3 de la misma área
            elif not validate_elective_availability(
                electivo_1, "electivo_1", cupos_electivos
            ):
                st.error(
                    f"Error. Electivo {electivo_1} sin cupo."
                )  # verificar si el electivo posee disponibilidad
            elif not validate_elective_availability(
                electivo_2, "electivo_2", cupos_electivos
            ):
                st.error(
                    f"Error. Electivo {electivo_2} sin cupo."
                )  # verificar si el electivo posee disponibilidad
            elif not validate_elective_availability(
                electivo_3, "electivo_3", cupos_electivos
            ):
                st.error(
                    f"Error. Electivo {electivo_2} sin cupo."
                )  # verificar si el electivo posee disponibilidad
            else:
                if insert_user_record(
                    name,
                    run,
                    email,
                    curso,
                    electivo_1,
                    electivo_2,
                    electivo_3,
                    electivo_fg,
                ):
                    return True  # insertar el registro en la base de datos de inscripciones
                else:
                    st.error(
                        "Error al insertar el registro en la base de datos"
                    )  # devolver un error si hubo un error al insertar el registro en la base de datos
