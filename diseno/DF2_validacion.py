"""DF2 convertido a Python: valida jugador, direccion, limites y pared.
Las coordenadas y la pared son un caso de prueba, no el mapa completo.
"""

ANCHO = 25
ALTO = 21
PARED_DE_PRUEBA = (12, 9)
TOTAL_JUGADORES = 5

# RF pendiente: validar jugada por formato y por reglas del mapa.

def validar_movimiento(jugador, direccion, x, y):
    """DF2: formato -> limites -> pared -> actualizar coordenadas.

    Direcciones numericas del RAPTOR:
    1 arriba, 2 abajo, 3 izquierda, 4 derecha.
    Devuelve (x, y, valido, mensaje). No mueve si hay error.
    """
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
    """Valida entradas numericas antes de utilizarlas (Input de RAPTOR)."""
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
    """Estado de prueba de DF2: (12,10) con pared (12,9)."""
    print("\n--- DF2: VALIDACION DE MOVIMIENTO ---")
    print("Laberinto 25 x 21; pared de prueba en (12,9).")
    x, y = 12, 10
    jugador = pedir_entero("ID de jugador conectado (1 a 5): ", 1, 5)
    while True:  # Loop: repetir la jugada mientras no sea valida
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
