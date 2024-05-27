import sqlite3

def verify_email(email):
    conn = sqlite3.connect("form_app.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM emails WHERE email = ?", (email,))
    result = cursor.fetchone()
    if result:
        conn.close()
        return True
        
    else:
        conn.close()
        return False

def insert_user(
    name, run, email, curso, electivo_1, electivo_2, electivo_3, electivo_fg
):
    conn = sqlite3.connect("form_app.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users_register (name, run, email, curso, electivo_1, electivo_2, electivo_3, electivo_fg) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (name, run, email, curso, electivo_1, electivo_2, electivo_3, electivo_fg),
    )
    conn.commit()
    conn.close()
    return True