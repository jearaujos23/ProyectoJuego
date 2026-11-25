ANCHO = 25
ALTO = 21
PARED_DE_PRUEBA = (12, 9)
TOTAL_JUGADORES = 5

# DF2 - RF pendiente de contrastar con los requisitos definitivos de la Fase 1.

def validar_movimiento(jugador, direccion, x, y):
    if not (1 <= jugador <= TOTAL_JUGADORES):
        return x, y, False, "Error de jugador: ID no conectado"
    if direccion not in (1, 2, 3, 4):
        return x, y, False, "Error de formato: direccion invalida"

    nx, ny = x, y
    if direccion == 1:
        ny -= 1
    elif direccion == 2:
        ny += 1
    elif direccion == 3:
        nx -= 1
    else:
        nx += 1

    if not (1 <= nx <= ANCHO and 1 <= ny <= ALTO):
        return x, y, False, "Movimiento rechazado: fuera del laberinto"
    if (nx, ny) == PARED_DE_PRUEBA:
        return x, y, False, "Movimiento bloqueado: pared"
    return nx, ny, True, "Movimiento aceptado"


def pedir_entero(mensaje, minimo, maximo):
    while True:
        valor = input(mensaje).strip()
        try:
            numero = int(valor)
        except ValueError:
            print("Error de formato: ingresa un numero entero.")
            continue
        if minimo <= numero <= maximo:
            return numero
        print(f"Valor fuera de rango: debe estar entre {minimo} y {maximo}.")


def ejecutar_df2():
    print("\n--- DF2: VALIDACION DE MOVIMIENTO ---")
    print("Laberinto 25 x 21; pared de prueba en (12,9).")
    x, y = 12, 10
    jugador = pedir_entero("ID de jugador conectado (1 a 5): ", 1, 5)
    while True:
        direccion = input("Direccion (1=arriba, 2=abajo, 3=izquierda, 4=derecha): ").strip()
        try:
            numero_direccion = int(direccion)
        except ValueError:
            print("Error de formato: direccion invalida")
            continue
        x_nuevo, y_nuevo, valido, aviso = validar_movimiento(
            jugador, numero_direccion, x, y
        )
        print(aviso)
        if valido:
            x, y = x_nuevo, y_nuevo
            print(f"Posicion resultante: ({x}, {y})")
            return x, y
        print("La posicion no cambia. Intenta de nuevo.")


if __name__ == "__main__":
    ejecutar_df2()
