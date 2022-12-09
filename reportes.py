import sqlite3 

conexion = sqlite3.connect("consultora.db")

cursor = conexion.cursor()

def trabajadores_activos():

    activo = True
    print("--------------- Listado de trabajadores activos ------------------\n")

    cursor.execute(f"select * from consultora where activo='{activo}'")

    print(cursor.fetchall())


def trabajadores_inactivos():
    activo = False
    print("--------------- Listado de trabajadores inactivos ------------------\n")

    cursor.execute(f"select * from consultora where activo='{activo}'")

    print(cursor.fetchall())

    
def desocupados_por_rango(edadMin, edadMax):
    if edadMin > edadMax:
        print("La edad minima no puede ser mayor a la maxima")
    else:
        print("--------------- Listado de trabajadores desocupados por rango de edad ------------------\n")

        print(f"Mostrando trabajadores entre {edadMin} y {edadMax} años")

        cursor.execute(f"select * from consultora where edad between '{edadMin}' and '{edadMax}'")

        print(cursor.fetchall())


def trabajadores_por_profesion(profesion):

    print(f"--------------- Listado de {profesion} ------------------\n")

    cursor.execute(f"select nombre, edad, dni, activo, codigo from consultora where profesion = '{profesion}'")

    print(cursor.fetchall())