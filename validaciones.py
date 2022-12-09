def validarIngresoEntero(opcion):
    while True:
        try:
            entero = int(input(opcion))
            break
        except ValueError:
            print("El valor ingresado no es un numero. Reintente")
    return entero


# Ver como pedir DNI de nuevo si esta mal

def validarFormatoDNI(dni):
    if len(f'{dni}') > 8:
        print("El DNI debe contener como maximo 8 numeros")
        return
    