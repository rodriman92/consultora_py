import sqlite3

conexion = sqlite3.connect("consultora.db")

cursor = conexion.cursor()

cursor.execute(""" create table if not exists
consultora (
    id integer primary key autoincrement,
    codigo text,
    nombre text,
    edad integer default 18,
    dni integer,
    profesion text,
    activo bool
) """)

conexion.close()