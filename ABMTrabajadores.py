from validaciones import validarIngresoEntero, validarFormatoDNI

def obtenerTrabajadores(nombreArchivo):
  try:
    archivo = open(nombreArchivo,"r")
  except FileNotFoundError:
    archivo = open(nombreArchivo,"a")
    archivo.write("1,Esteban,21,34567567,Programador,true")
    archivo.close()
    archivo = open(nombreArchivo,"r")

#Nombre,edad,dni,profesion,activo(true,false)
  trabajadores=[]
  for linea in archivo.readlines():
    trabajador=linea.replace('\n','') # "6Gato34"
    trabajador=trabajador.split(",") # ["6Gato34"]
    trabajador = {"codigo":int(trabajador[0]),"nombre":trabajador[1],"edad":int(trabajador[2]),"dni":int(trabajador[3]),"profesion":trabajador[4],"activo":trabajador[5]}
    trabajadores.append(trabajador)
  archivo.close()
  return trabajadores


def agregarTrabajador(listado):
  codigo = validarIngresoEntero("codigo: ")
  nombre=input("nombre: ")
  edad = validarIngresoEntero("Edad: ")
  # Controlar que no se ingrese el mismo dni (FALTA)
  dni=validarIngresoEntero("DNI: ")
  validarFormatoDNI(dni)
  profesion=input("profesion: ") # Ver si se puede controlar para que sea solo letras

  # Pone como estado true o false presionando la S o la N
  activo=input("Activo? Presione [S] para SI o [N] para NO: ")
  activo = activo.upper()
  if activo == "S":
    activo = True
  elif activo == "N":
    activo = False
  else:
    print("La opcion no es correcta")


  # Crea al trabajador y lo guarda en el listado
  trabajador = {"codigo":codigo,"nombre":nombre, "edad":edad, "dni":dni, "profesion":profesion, "activo":activo}
  listado.append(trabajador)

  # Agrega al trabajador a el archivo
  archivo = open("trabajadores.dat","a")
  linea = f"\n{codigo},{trabajador['nombre']},{trabajador['edad']},{trabajador['dni']},{trabajador['profesion']},{trabajador['activo']}"
  archivo.write(linea)
  archivo.close()





def modificarTrabajador(listado, codigo):
  for trabajador in listado:
    if trabajador["codigo"] == codigo:
      print(trabajador)
      nombre = input("Nombre: (Presiona Enter para no modificar) ")
      if nombre == "":
        nombre = trabajador["nombre"]
      
      edad = validarIngresoEntero("Edad: ")
      dni = validarIngresoEntero("DNI: ")
      validarFormatoDNI(dni)
      profesion=input("profesion: ")
      ## EDITAADO ##
      # Pone como estado true o false presionando S o N
      activo=input("Activo? Presione [S] para SI o [N] para NO: ")
      if activo == "S":
        activo = True
      else:
        activo = False
      # Grabar en listado las modificaciones
      trabajador["nombre"] = nombre
      trabajador["edad"] = edad
      trabajador["profesion"] = profesion
      trabajador["activo"]=activo
      break

  # Guarda modificacion en archivo
  
  archivo = open("trabajadores.dat", "w")
  contenido = []

  for trabajador in listado:
    linea = f"\n{trabajador['codigo']},{trabajador['nombre']}, {trabajador['edad']}, {trabajador['dni']}, {trabajador['profesion']}, {trabajador['activo']}"
    contenido.append(linea)

  contenido[0] = contenido[0].replace("\n", "")

  archivo.writelines(contenido)

  archivo.close()

   

  



def modificarStatusTrabajador(listado, dni):
  for trabajador in listado:
    if trabajador["dni"] == dni:
      print(trabajador)
      ## EDITADO ##
      # Cambio en modificar, toma valores bool #
      activo=input("Activo? Presione [S] para SI o [N] para NO o Enter para omitir: ")
      if activo == "S":
        activo = True
      else:
        activo = False
      if activo == "":
        activo = trabajador["activo"]
      
      # Grabar en listado las modificaciones
      trabajador["activo"]=activo
      break
  print("El DNI No se encuentra registrado")



  # Grabar en archivo
  archivo = open("trabajadores.dat","w")
  contenido = []
  for empleadito in listado:
    linea = f"\n{empleadito['codigo']},{empleadito['nombre']},{empleadito['edad']},{empleadito['dni']},{empleadito['profesion']},{empleadito['activo']}"
    contenido.append(linea)

  contenido[0] = contenido[0].replace("\n","")
  archivo.writelines(contenido) 

  archivo.close()




def eliminarTrabajador(listado, codigo):
  for trabajador in listado:
    if trabajador["codigo"] == codigo:
      print(trabajador)
      listado.remove(trabajador)
      break

  print(listado) 


  
  # Eliminar en archivo

  archivo = open("trabajadores.dat","w")
  contenido = []
  for empleadito in listado:
    linea = f"\n{empleadito['codigo']},{empleadito['nombre']},{empleadito['edad']},{empleadito['dni']},{empleadito['profesion']},{empleadito['activo']}"
    contenido.append(linea)

  contenido[0] = contenido[0].replace("\n","")
  archivo.writelines(contenido) 

  archivo.close()

