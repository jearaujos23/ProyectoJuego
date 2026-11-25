def mostrar_menu():
    while True:
        print("\n=== PAC-MAN MULTIJUGADOR COMPETITIVO ===")
        print("1. Jugar")
        print("2. Salir")
        opcion = input("Elige una opcion (1 o 2): ").strip()

        if opcion == "1":
            print("Partida de 5 jugadores: 1 Pac-Man y 4 fantasmas.")
            print("La partida completa y la red se programaran en la Fase 4.")
        elif opcion == "2":
            print("Saliendo del juego.")
            break
        else:
            print("Opcion invalida. Escribe 1 o 2.")


if __name__ == "__main__":
    mostrar_menu()
