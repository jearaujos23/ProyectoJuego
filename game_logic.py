"""
game_logic.py - Lógica de la partida de "Pac-Man multijugador competitivo".

Traduce a Python dos diagramas de la Fase 2:
  - DF2 (diseno/DF2_validacion.rap): validación de la jugada.
  - DF3 (diseno/DF3_fin.rap): fin de la ronda y de la partida.

Cada parte empieza con su estado de ejemplo asignado al inicio, igual que en
RAPTOR. La partida completa (el bucle de turnos del modo local) se programa en
la Fase 4; aquí solo se prueban estas dos decisiones por separado.

Ejecutar con:  python game_logic.py
"""


def leer_entero(mensaje):
    """GET de RAPTOR: devuelve un número entero, o None si el texto no es un número."""
    texto = input(mensaje).strip()
    if texto.lstrip("-").isdigit():
        return int(texto)
    return None


def en_rango(valor, minimo, maximo):
    """True si el valor es un número y está entre minimo y maximo (incluidos)."""
    return valor is not None and minimo <= valor <= maximo


# ----------------------------------------------------------------------
# DF2 - Validación de la jugada  (RF-04, RF-05 y RF-06)
# ----------------------------------------------------------------------
def df2_validacion():
    print("DF2 - MOVIMIENTO Y VALIDACION")
    print("Laberinto de prueba 25x21. Pared en 12,9.")

    # Estado de ejemplo asignado al inicio (igual que en RAPTOR)
    x = 12            # columna actual del jugador
    y = 10            # fila actual del jugador
    aceptado = 0      # 1 cuando se acepta un movimiento

    # Loop: se vuelve a pedir la jugada mientras sea inválida (RF-04, RF-05)
    while aceptado == 0:
        jugador = leer_entero("ID de participante conectado (1 a 5): ")   # RF-04

        if en_rango(jugador, 1, 5):
            direccion = leer_entero("Direccion: 1 arriba, 2 abajo, 3 izquierda, 4 derecha: ")

            # Validación por FORMATO (RF-05): la dirección debe ser 1, 2, 3 o 4
            if en_rango(direccion, 1, 4):
                nx = x
                ny = y
                if direccion == 1:
                    ny = y - 1
                if direccion == 2:
                    ny = y + 1
                if direccion == 3:
                    nx = x - 1
                if direccion == 4:
                    nx = x + 1

                # Validación por REGLAS (RF-05): dentro del laberinto y sin pared
                if 1 <= nx <= 25 and 1 <= ny <= 21:
                    if nx == 12 and ny == 9:
                        print("Movimiento bloqueado: pared")
                    else:
                        x = nx            # RF-06: se actualiza la posición
                        y = ny
                        aceptado = 1
                        print("Movimiento aceptado")
                else:
                    print("Movimiento rechazado: fuera del laberinto")
            else:
                print("Error de formato: direccion invalida")
        else:
            print("Error de jugador: ID no conectado")

    print("Posicion resultante:")
    print(x)
    print(y)


# ----------------------------------------------------------------------
# DF3 - Fin de la ronda, rotación de roles y ganador  (RF-07 a RF-11)
# ----------------------------------------------------------------------
def df3_fin():
    print("DF3 - FIN DE RONDA / ROTACION / GANADOR")

    # Estado de ejemplo asignado al inicio (igual que en RAPTOR)
    datos_validos = 0

    # Loop: se repite hasta tener datos de la ronda válidos
    while datos_validos == 0:
        ronda = leer_entero("Numero de ronda (1 a 5): ")
        restante = leer_entero("Segundos restantes (0 a 300): ")
        capturados = leer_entero("Fantasmas capturados (0 a 4): ")
        if en_rango(ronda, 1, 5) and en_rango(restante, 0, 300) and en_rango(capturados, 0, 4):
            datos_validos = 1
        else:
            print("Datos no validos: repetir")

    # Decisión de DF3: ¿la ronda sigue? (RF-07, RF-10)
    if restante > 0 and capturados < 4:
        print("La ronda continua")
    else:
        # La ronda termina por captura o por tiempo (RF-08, RF-09)
        if capturados == 4:
            print("FIN: cuatro fantasmas capturados")
        else:
            print("FIN: se cumplieron los 300 segundos")

        if ronda < 5:
            # Rotación de roles: en la siguiente ronda es Pac-Man el jugador "ronda" (RF-11)
            ronda = ronda + 1
            rol_pacman = ronda
            print("Siguiente ronda")
            print(ronda)
            print("Pac-Man: jugador")
            print(rol_pacman)
        else:
            print("Cinco rondas terminadas: comparar puntuaciones")

            # Loop: puntos acumulados válidos (no negativos)
            puntos_validos = 0
            while puntos_validos == 0:
                p1 = leer_entero("Puntos acumulados del jugador 1: ")
                p2 = leer_entero("Puntos acumulados del jugador 2: ")
                p3 = leer_entero("Puntos acumulados del jugador 3: ")
                p4 = leer_entero("Puntos acumulados del jugador 4: ")
                p5 = leer_entero("Puntos acumulados del jugador 5: ")
                if (en_rango(p1, 0, 10**9) and en_rango(p2, 0, 10**9) and en_rango(p3, 0, 10**9)
                        and en_rango(p4, 0, 10**9) and en_rango(p5, 0, 10**9)):
                    puntos_validos = 1
                else:
                    print("Puntos negativos: repetir")

            # Búsqueda del mayor puntaje y de su jugador
            mayor = p1
            ganador = 1
            if p2 > mayor:
                mayor = p2
                ganador = 2
            if p3 > mayor:
                mayor = p3
                ganador = 3
            if p4 > mayor:
                mayor = p4
                ganador = 4
            if p5 > mayor:
                mayor = p5
                ganador = 5

            # ¿Cuántos jugadores tienen el puntaje máximo? (empate en primer lugar)
            cantidad_maximos = 0
            if p1 == mayor:
                cantidad_maximos = cantidad_maximos + 1
            if p2 == mayor:
                cantidad_maximos = cantidad_maximos + 1
            if p3 == mayor:
                cantidad_maximos = cantidad_maximos + 1
            if p4 == mayor:
                cantidad_maximos = cantidad_maximos + 1
            if p5 == mayor:
                cantidad_maximos = cantidad_maximos + 1

            if cantidad_maximos > 1:
                print("EMPATE en primer lugar: desempate pendiente")
            else:
                print("GANADOR: JUGADOR")
                print(ganador)
                print("TOTAL")
                print(mayor)


# ----------------------------------------------------------------------
# Programa principal: cada diagrama se prueba por separado, como en RAPTOR
# ----------------------------------------------------------------------
if __name__ == "__main__":
    df2_validacion()
    print()
    df3_fin()
