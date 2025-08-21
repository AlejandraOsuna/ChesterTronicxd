import sqlite3
from datetime import datetime

DB_NAME = "inventario.db"

def crear_tabla():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            cantidad INTEGER NOT NULL,
            descripcion TEXT,
            hora_registro TEXT
        )
    """)
    conn.commit()
    conn.close()

def agregar_item(nombre, cantidad, descripcion):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute("INSERT INTO inventario (nombre, cantidad, descripcion, hora_registro) VALUES (?, ?, ?, ?)",
              (nombre, cantidad, descripcion, hora))
    conn.commit()
    conn.close()

def obtener_items():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM inventario")
    items = c.fetchall()
    conn.close()
    return items

def eliminar_item(item_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("DELETE FROM inventario WHERE id=?", (item_id,))
    conn.commit()
    conn.close()

def editar_item(item_id, nombre, cantidad, descripcion):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    c.execute(
        "UPDATE inventario SET nombre=?, cantidad=?, descripcion=?, hora_registro=? WHERE id=?",
        (nombre, cantidad, descripcion, hora, item_id)
    )
    conn.commit()
    conn.close()