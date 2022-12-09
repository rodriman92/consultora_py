from validaciones import validarIngresoEntero, validarFormatoDNI
from decoraciones import decorar
import sqlite3


conexion = sqlite3.connect("consultora.db")
cursor = conexion.cursor()

def obtenerTrabajadores():
  try:
    
    cursor.execute("select * from consultora")
    print(cursor.fetchall())
  except FileNotFoundError:
    print("Error al obtener los datos")


def agregarTrabajador():
  try:  
    codigo = validarIngresoEntero("codigo: ")
    nombre=input("nombre: ")
    edad = validarIngresoEntero("Edad: ")
    dni=validarIngresoEntero("DNI: ")
    validarFormatoDNI(dni)
    profesion=input("profesion: ") 

    # Pone como estado true o false presionando la S o la N
    activo=input("Activo? Presione [S] para SI o [N] para NO: ")
    activo = activo.upper()
    if activo == "S":
      activo = True
    elif activo == "N":
      activo = False
    else:
      print("La opcion no es correcta")

    # Agregar a la base de datos

    cursor.execute(f"insert into consultora (nombre, edad, dni, profesion, activo, codigo) values ('{nombre}', '{edad}', '{dni}', '{profesion}', '{activo}', '{codigo}')")

    conexion.commit()
  except:
    print("Ocurrio un error al cargar el registro.")


def modificarTrabajador(id):

    cursor.execute(f"select * from consultora where id = '{id}'")
    print("El registro a modificar es: \n")
    print(cursor.fetchall())

    nombre = input("Nombre (Enter para no modificar): ")
    if nombre != "":
      cursor.execute(f"update consultora set nombre = '{nombre}' where id = '{id}'")

    edad = input("Edad (Enter para no modificar): ")
    if edad != "":
      cursor.execute(f"update consultora set edad = '{edad}' where id = '{id}'")

    dni = input("DNI (Enter para no modificar): ")
    if dni != "":
      validarFormatoDNI(dni)
      cursor.execute(f"update consultora set dni = '{dni}' where id = '{id}'")

    profesion=input("Profesion (Enter para no modificar): ")
    if profesion != "":
      cursor.execute(f"update consultora set profesion = '{profesion}' where id = '{id}'")

    activo=input("Activo? Presione [S] para SI o [N] para NO: ")
    activo = activo.upper()
    if activo == "S":
      activo = True
    elif activo == "N":
      activo = False
    else:
      print("La opcion no es correcta")
    

    cursor.execute(f"update consultora set activo='{activo}' where id='{id}'")

    try:

      conexion.commit()

      print(f"El registro se actualizo correctamente \n")

      cursor.execute(f"select * from consultora where id = '{id}'")

      print(cursor.fetchall())
      
    except:
      print("Ocurrio un error al actualizar el registro. Reintente")



def modificarStatusTrabajador(dni):
  try:
    print("Registro encontrado: \n")

    cursor.execute(f"select * from consultora where dni = '{dni}'")

    print(cursor.fetchall())

    opcion = input("Presione S para marcarlo como ACTIVO o N para marcarlo como INACTIVO: ")
    opcion.upper()

    if opcion == "S":
      opcion = True
      leyenda = "ACTIVO"
    elif opcion == "N":
      opcion = False
      leyenda = "INACTIVO"
    else:
      print("La opcion no es correcta. ")

    cursor.execute(f"update consultora set activo = '{opcion}' where dni = '{dni}'")

    print(f"Registro actualizado \nEl estado del trabajador {dni} es {leyenda}")

    conexion.commit()

    conexion.close()
  except:
    print("El dni no se encuentra registrado en el sistema")



def eliminarTrabajador(id):
  try:
      print("Registro encontrado: \n")
      cursor.execute(f"select * from consultora where id = '{id}'")
      print(cursor.fetchall())

      print("Eliminando ...")


      cursor.execute(f"delete from consultora where id = '{id}'")

      print(f"Registro eliminado")

      conexion.commit()

      conexion.close()
  except:
      print("El dni no se encuentra registrado en el sistema")

