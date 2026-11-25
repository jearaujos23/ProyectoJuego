"""
client.py - Cliente (Jugadores 2 a 5) de "Pac-Man multijugador competitivo".

POR AHORA SOLO COMENTARIO: los sockets se programan en la Fase 4.

Lo que hará este archivo (según el diagrama de arquitectura de la Fase 2):
  - Ejecutarse en las VM 2 a 5 (Jugador 2 a Jugador 5), una por participante.
  - Conectarse por TCP al servidor 192.168.56.10:5000 (RF-02).
  - Enviar al servidor la dirección que el jugador presiona (RF-04).
  - Recibir y mostrar el rol, el estado, los avisos de validación y los resultados (RF-05 a RF-11).

Mensajes que enviará el cliente al servidor:
  CONECTAR|J2             al entrar a la partida (el número cambia según el jugador)
  MOV|J2|ARRIBA           cuando el jugador presiona una dirección (ARRIBA, ABAJO, IZQUIERDA o DERECHA)
"""
