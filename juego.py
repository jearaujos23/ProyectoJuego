"""
juego.py - Punto de entrada del proyecto "Pac-Man multijugador competitivo".

Traduce a Python el menú de DF1 (diseno/DF1_partida.rap):
  - El menú se repite hasta que se elige "Salir".
  - La opción "Jugar" solo muestra un mensaje por ahora: la partida completa
    (rondas, roles y turnos del modo local) se programa en la Fase 4.

Requisito de la Fase 1 que cubre: RF-01 (opción del menú).
Ejecutar con:  python juego.py
"""

# --- DF1: mensajes iniciales (PUT) ---
print("DF1 - PAC-MAN MULTIJUGADOR COMPETITIVO")
print("Simulacion local; TCP y reloj real se documentan aparte")

# --- DF1: estado de ejemplo asignado al inicio (menu <- 0 en RAPTOR) ---
menu = ""

# --- DF1: Loop del menú, termina cuando menu = 2 (RF-01) ---
while menu != "2":
    print("Menu 1 Jugar / 2 Salir")
    menu = input("Elige una opcion: ").strip()   # GET menu

    if menu == "1":
        # En DF1 aquí empieza la partida completa; en la Fase 3 solo se avisa.
        print("Jugar: la partida completa se programa en la Fase 4.")
    elif menu == "2":
        print("Salir")
    else:
        # Cualquier texto o número distinto de 1 y 2 vuelve a pedir la opción.
        print("Opcion invalida: use 1 o 2")
