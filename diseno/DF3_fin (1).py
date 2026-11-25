from DF2_validacion import pedir_entero

TOTAL_RONDAS = 5
DURACION_RONDA = 300
FANTASMAS_POR_RONDA = 4
PUNTOS_BOLITA = 50
PUNTOS_CADA_5_SEGUNDOS = 20
BONO_300_SEGUNDOS = 200

# DF3 - RF pendiente de contrastar con los requisitos definitivos de la Fase 1.

def puntaje_fantasma(bolitas, segundos_sobrevividos):
    if bolitas < 0 or not (0 <= segundos_sobrevividos <= DURACION_RONDA):
        raise ValueError("Bolitas o segundos fuera de rango")
    puntos = bolitas * PUNTOS_BOLITA
    puntos += (segundos_sobrevividos // 5) * PUNTOS_CADA_5_SEGUNDOS
    if segundos_sobrevividos == DURACION_RONDA:
        puntos += BONO_300_SEGUNDOS
    return puntos


def puntaje_pacman(capturas, puntos_por_captura):
    if capturas < 0 or capturas > 4 or puntos_por_captura < 0:
        raise ValueError("Valor de captura fuera de rango")
    return capturas * puntos_por_captura


def ganador_cinco(p1, p2, p3, p4, p5):
    puntos = (p1, p2, p3, p4, p5)
    if any(p < 0 for p in puntos):
        raise ValueError("La puntuacion no puede ser negativa")
    mayor = max(puntos)
    ganadores = [i for i, p in enumerate(puntos, start=1) if p == mayor]
    if len(ganadores) > 1:
        return f"Empate en primer lugar: jugadores {', '.join(map(str, ganadores))} ({mayor} puntos)"
    return f"GANADOR: Jugador {ganadores[0]} con {mayor} puntos"


def evaluar_df3(ronda, restantes, capturados, puntuaciones=None):
    if not (1 <= ronda <= TOTAL_RONDAS):
        raise ValueError("Ronda debe ser 1 a 5")
    if not (0 <= restantes <= DURACION_RONDA):
        raise ValueError("Restantes debe ser 0 a 300")
    if not (0 <= capturados <= FANTASMAS_POR_RONDA):
        raise ValueError("Capturados debe ser 0 a 4")

    if restantes > 0 and capturados < FANTASMAS_POR_RONDA:
        return "La ronda continua"
    if capturados == FANTASMAS_POR_RONDA:
        motivo = "FIN: cuatro fantasmas capturados"
    else:
        motivo = "FIN: se cumplieron los 300 segundos"

    if ronda < TOTAL_RONDAS:
        siguiente = ronda + 1
        return f"{motivo}. Siguiente ronda: {siguiente}. Pac-Man: jugador {siguiente}"

    if puntuaciones is None:
        return f"{motivo}. Cinco rondas terminadas: faltan puntuaciones"
    if len(puntuaciones) != 5:
        raise ValueError("Se necesitan las cinco puntuaciones")
    return f"{motivo}. Cinco rondas terminadas. " + ganador_cinco(*puntuaciones)


def ejecutar_df3():
    print("\n--- DF3: FIN DE RONDA Y GANADOR ---")
    ronda = pedir_entero("Ronda actual (1 a 5): ", 1, 5)
    restantes = pedir_entero("Segundos RESTANTES (0 a 300): ", 0, 300)
    capturados = pedir_entero("Fantasmas capturados (0 a 4): ", 0, 4)
    fin = restantes == 0 or capturados == 4
    if fin and ronda == 5:
        puntajes = tuple(
            pedir_entero(f"Puntos acumulados del jugador {i}: ", 0, 1000000)
            for i in range(1, 6)
        )
        print(evaluar_df3(ronda, restantes, capturados, puntajes))
    else:
        print(evaluar_df3(ronda, restantes, capturados))


def ejecutar_puntos():
    print("\n--- PUNTOS DE FANTASMAS ---")
    bolitas = pedir_entero("Bolitas recogidas: ", 0, 1000000)
    segundos = pedir_entero("Segundos sobrevividos (0 a 300): ", 0, 300)
    print("Puntos del fantasma:", puntaje_fantasma(bolitas, segundos))
    print("Capturas de Pac-Man: valor configurable, aun no confirmado.")


if __name__ == "__main__":
    ejecutar_df3()
