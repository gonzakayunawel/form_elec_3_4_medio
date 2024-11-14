import streamlit as st
import re
import requests

API_URL = st.secrets["API_URL"]
# API_URL = st.secrets["LOCAL_API_URL"]
CUPO_ELECTIVO = int(st.secrets["CUPOS"])


# Definir una función para validar el RUN chileno
def is_valid_run(run):
    # Definir la expresión regular para un RUN chileno
    run_regex = r"^\d{7,8}-[\dKk]$"

    # Compilar la expresión regular
    pattern_run = re.compile(run_regex)

    return bool(pattern_run.fullmatch(run))

# Definir una función para validar que los electivos no sean los 3 de la misma área
def validate_electivos(electivo_1: str, electivo_2: str, electivo_3: str, electivo_fg: str) -> bool:
    """ Validar que los electivos no sean los 3 de la misma área

    Args:
        electivo_1 (str): Electivo 1
        electivo_2 (str): Electivo 2
        electivo_3 (str): Electivo 3
        electivo_fg (str): Electivo de formación general

    Returns:
        bool: True si los electivos no son los 3 de la misma área, False en caso contrario
    """
    if electivo_1 is None or electivo_2 is None or electivo_3 is None or electivo_fg is None:
        return False
    elif electivo_1[:6] == electivo_2[:6] == electivo_3[:6]:
        return False
    else:
        return True

# Verificar si el correo electrónico es válido para inscribirse
def verify_email(email:str) -> bool:
    """ Verificar si el correo electrónico es válido para inscribirse

    Args:
        email (str): Correo electrónico

    Returns:
        bool: True si el correo electrónico es válido, False en caso contrario
    """
    try:
        response = requests.get(f"{API_URL}/verify_email/{email}")
        response.raise_for_status()
        data = response.json()

        return True if data["message"] == True else False

    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Error en la solicitud: {err}')
    except ValueError:
        print('Error al procesar JSON: la respuesta no es un JSON válido')

def verify_user(run: str, email: str, curso: str) -> bool:
    """ Verificar si el RUN, email y curso corresponden al usuario

    Args:
        run (str): RUN
        email (str): Correo electrónico
        curso (str): Curso

    Returns:
        bool: True si corresponden, False en caso contrario
    """
    run = run.replace("-", "")
    try:
        response = requests.get(f"{API_URL}/verify_user/{run}/{email}/{curso}")
        response.raise_for_status()
        data = response.json()

        return True if data["message"] == True else False

    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Error en la solicitud: {err}')
    except ValueError:
        print('Error al procesar JSON: la respuesta no es un JSON válido')

# Verificar si el email ya está registrado
def check_student_record( email: str) -> bool:
    """ Verificar si el email ya está registrado

    Args:

        email (str): Correo electrónico

    Returns:
        bool: True si está registrado, False caso contrario
    """
    try:
        response = requests.get(f"{API_URL}/check_student_record/{email}")
        response.raise_for_status()
        data = response.json()

        return True if data["message"] == True else False

    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Error en la solicitud: {err}')
    except ValueError:
        print('Error al procesar JSON: la respuesta no es un JSON válido')

# Verificar que hay cupos disponibles para el electivo
def validate_elective_availability(electivo_seleccionado: str, columna_electivo: str, cupos_electivos: int) -> bool:
    """ Verificar que hay cupos disponibles para el electivo

    Args:
        electivo (str): Electivo
        electivo_name (str): Nombre del electivo
        cupos_electivos (int): Número de cupos disponibles para el electivo

    Returns:
        bool: True si hay cupos disponibles, False en caso contrario
    """
    try:
        response = requests.get(f"{API_URL}/check_elective_class_availability/{electivo_seleccionado}/{columna_electivo}/{cupos_electivos}")
        response.raise_for_status()
        data = response.json()

        return True if data["message"] == True else False

    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Error en la solicitud: {err}')
    except ValueError:
        print('Error al procesar JSON: la respuesta no es un JSON válido')

# Verificar que hay cupos disponibles para el electivo de formación general
def validate_elective_availability_fg(electivo_seleccionado: str, curso: str, cupos_electivos_fg: int) -> bool:
    """ Verificar que hay cupos disponibles para el electivo de formación general

    Args:
        electivo (str): Electivo
        electivo_name (str): Nombre del electivo
        cupos_electivos (int): Número de cupos disponibles para el electivo

    Returns:
        bool: True si hay cupos disponibles, False en caso contrario
    """
    try:
        response = requests.get(f"{API_URL}/check_elective_class_availability_fg/{electivo_seleccionado}/{curso}/{cupos_electivos_fg}")
        response.raise_for_status()
        data = response.json()

        return True if data["message"] == True else False

    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Error en la solicitud: {err}')
    except ValueError:
        print('Error al procesar JSON: la respuesta no es un JSON válido')

# Vetificar si el estudiante está inscrito en el electivo anterior
def check_student_enrolled_in_previous_elective(run: str, electivo: str) -> bool:
    """ Vetificar si el estudiante está inscrito en el electivo anterior

    Args:
        run (str): RUN
        electivo (str): Electivo

    Returns:
        bool: True si está inscrito, False en caso contrario
    """
    try:
        response = requests.get(f"{API_URL}/check_student_enrolled_in_previous_elective/{run}/{electivo}")
        response.raise_for_status()
        data = response.json()

        return True if data["message"] == True else False

    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Error en la solicitud: {err}')
    except ValueError:
        print('Error al procesar JSON: la respuesta no es un JSON válido')

# Insertar registro en la base de datos de inscripciones
def insert_user_record(
    name,
    run,
    email,
    curso,
    electivo_1,
    electivo_2,
    electivo_3,
    electivo_fg,
):
    """ Insertar registro en la base de datos de inscripciones

    Args:
        name (str): Nombre
        run (str): RUN
        email (str): Correo electrónico
        curso (str): Curso
        electivo_1 (str): Electivo 1
        electivo_2 (str): Electivo 2
        electivo_3 (str): Electivo 3
        electivo_fg (str): Electivo de formación general

    Returns:
        bool: True si se insertó correctamente, False en caso contrario
    """
    try:
        response = requests.post(f"{API_URL}/insert_user_record", json={
            "name": name,
            "run": run,
            "email": email,
            "curso": curso,
            "electivo_1": electivo_1,
            "electivo_2": electivo_2,
            "electivo_3": electivo_3,
            "electivo_fg": electivo_fg,
        })
        response.raise_for_status()
        data = response.json()

        return True if data["message"] == True else False

    except requests.exceptions.HTTPError as http_err:
        print(f'Error HTTP: {http_err}')
    except requests.exceptions.RequestException as err:
        print(f'Error en la solicitud: {err}')
    except ValueError:
        print('Error al procesar JSON: la respuesta no es un JSON válido')

# Validar el formulario
def validate_form(
    name,
    run,
    email,
    curso,
    electivo_1,
    electivo_2,
    electivo_3,
    electivo_fg
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
        if not verify_user(run, email, curso):
            st.error(
                "El RUN, email o curso no se corresponden. Verifca que tu RUN, correo y curso sean correctos."
            )

        else:
            if check_student_record(email):
                st.error(
                    "El email ingresado ya fue registrado"
                )  # verificar si el email ya está en la base de datos de inscripciones

            elif not validate_electivos(electivo_1, electivo_2, electivo_3, electivo_fg):
                st.error(
                    "Los electivos no pueden ser los 3 de la misma área o hay un electivo no seleccionado. Por favor, selecciona los electivos que quieres inscribirte."
                )  # verificar si los electivos no son los 3 de la misma área

            elif not validate_elective_availability(
                electivo_1, "electivo_1", CUPO_ELECTIVO
            ):
                st.error(
                    f"Error. Electivo: {electivo_1} sin cupo."
                )  # verificar si el electivo posee disponibilidad

            elif not validate_elective_availability(
                electivo_2, "electivo_2", CUPO_ELECTIVO
            ):
                st.error(
                    f"Error. Electivo: {electivo_2} sin cupo."
                )  # verificar si el electivo posee disponibilidad

            elif not validate_elective_availability(
                electivo_3, "electivo_3", CUPO_ELECTIVO
            ):
                st.error(
                    f"Error. Electivo: {electivo_3} sin cupo."
                )  # verificar si el electivo posee disponibilidad

            elif validate_elective_availability_fg(
                electivo_fg, curso, CUPO_ELECTIVO
            ):
                st.error(
                    f"Error. Electivo: {electivo_fg} sin cupo para el curso: {curso}."
                )
            elif check_student_enrolled_in_previous_elective(run, electivo_1):
                st.error(
                    f"Error. El electivo {electivo_1} ya fue realizado en el año anterior."
                )
            elif check_student_enrolled_in_previous_elective(run, electivo_2):
                st.error(
                    f"Error. El electivo {electivo_2} ya fue realizado en el año anterior."
                )
            elif check_student_enrolled_in_previous_elective(run, electivo_3):
                st.error(
                    f"Error. El electivo {electivo_3} ya fue realizado en el año anterior."
                )
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
                        "Error al registrar la inscripción. Inténtalo de nuevo."
                    )  # devolver un error si hubo un error al insertar el registro en la base de datos
