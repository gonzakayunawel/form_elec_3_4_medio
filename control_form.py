import sqlite3

def verify_email(email, table="emails"):
    conn = sqlite3.connect("form_app.db")
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT * FROM {table} WHERE email = ?", (email,))
        result = cursor.fetchone()
        if result:
            return True
    except Exception as e:
        raise e
    finally:
        conn.close()

def insert_user_record(name, run, email, curso, electivo_1, electivo_2, electivo_3, electivo_fg):
    conn = sqlite3.connect("form_app.db")
    cursor = conn.cursor()

    if verify_email(email, table="emails"):
        try:
            cursor.execute(
                "INSERT INTO users_register (name, run, email, curso, electivo_1, electivo_2, electivo_3, electivo_fg) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (name, run, email, curso, electivo_1, electivo_2, electivo_3, electivo_fg),
            )
            conn.commit()  # Guarda los cambios
            return True  # Devuelve True si la inserción fue exitosa
        except Exception as e:
            raise e  # Devuelve False si hubo un error
        finally:
            conn.close()  # Asegúrate de cerrar la conexión
    else:
        conn.close()
        return False  # Devuelve False si el email ya está en uso