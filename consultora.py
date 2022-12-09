from validaciones import validarIngresoEntero, validarFormatoDNI
from decoraciones import decorar
from ABMTrabajadores import agregarTrabajador,modificarTrabajador,obtenerTrabajadores, eliminarTrabajador,modificarStatusTrabajador
from menues import menuPrincipal, menuGestionTrabajador, menuReportes,menuActualizarEstadoDelTrabajador
from reportes import trabajadores_activos, trabajadores_inactivos, desocupados_por_rango, trabajadores_por_profesion

listadoDePersonas = obtenerTrabajadores()

while True:

    decorar()
    menuPrincipal()
    opcion = validarIngresoEntero("Ingrese una opcion: ")

    if opcion == 0:
        opcionSalir = input("Está seguro que desea salir? [S]i/[N]o: ")
        opcionSalir = opcionSalir.upper()
        if opcionSalir == "S":
            print("Saliendo...")
            break
        elif opcionSalir == "N":
            continue
        else:
            print("La opcion no es correcta. Reintente")

    elif opcion == 1:
        decorar()
        while True:
            menuGestionTrabajador()
            opcionGestionTrabajador = validarIngresoEntero("Seleccione una opcion: ")

            if opcionGestionTrabajador == 0:
                break
            elif opcionGestionTrabajador == 1:
                print("Ingresar nuevo trabajador")
                agregarTrabajador()
            elif opcionGestionTrabajador == 2:
                print("Modificar datos de trabajador")
                id=validarIngresoEntero("Ingrese el ID del trabajador a modificar: ")
                modificarTrabajador(id)
            elif opcionGestionTrabajador == 3:
                print("Eliminar trabajador")
                id=validarIngresoEntero("Ingrese el ID del trabajador a eliminar: ")
                eliminarTrabajador(id)
            else:
                print("La opcion no es correcta. Reintente")
                continue

    elif opcion == 2:
        decorar()
        while True:
            menuReportes()
            opcionReportes = validarIngresoEntero("Seleccione una opcion: ")

            if opcionReportes == 0:
                break
            elif opcionReportes == 1:
                print("Mostrando reporte de trabajadores activos")
                trabajadores_activos()
            elif opcionReportes == 2:
                print("Mostrando reporte de personas desocupadas")
                trabajadores_inactivos()
            elif opcionReportes == 3:
                print("Mostrando reporte de desocupados por rango de edad")
                edadMin = validarIngresoEntero("Ingrese una edad minima: ")
                edadMax = validarIngresoEntero("Ingrese una edad maxima: ")
                desocupados_por_rango(edadMin, edadMax)
            elif opcionReportes == 4:
                print("Mostrando reporte de trabajadores por profesion")
                profesion=input("Ingrese la profesion: ")
                trabajadores_por_profesion(profesion)
            else:
                print("La opcion ingresada no es valida. Reintente")
                continue

    elif opcion == 3:
        decorar()
        print("Actualizar estado del trabajador")
        while True:
            menuActualizarEstadoDelTrabajador()
            opcionActualizarEstadoDelTrabajador = validarIngresoEntero("Seleccione una opcion: ")
            if opcionActualizarEstadoDelTrabajador == 1:
                print("Modificar status del trabajador")
                dni=validarIngresoEntero("DNI del trabajador a modificar: ")
                modificarStatusTrabajador(dni)

            elif opcionActualizarEstadoDelTrabajador == 0:
                break
            else:
                print("La opcion no es correcta, Reintente")
                continue

    else:
        print("La opcion ingresada no es correcta. Reintente")