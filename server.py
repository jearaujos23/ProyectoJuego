"""
server.py - Servidor (Jugador 1) de "Pac-Man multijugador competitivo".

POR AHORA SOLO COMENTARIO: los sockets se programan en la Fase 4.

Lo que hará este archivo (según el diagrama de arquitectura de la Fase 2):
  - Ejecutarse en la VM 1 (Jugador 1 = servidor), IP 192.168.56.10, puerto 5000, socket TCP.
  - Aceptar las conexiones de los cuatro clientes por la red LAN (RF-02).
  - Asignar los roles (un Pac-Man y cuatro fantasmas) y rotarlos en cada ronda (RF-03, RF-11).
  - Recibir los movimientos, validarlos con game_logic.py (DF2) y actualizar el estado (RF-04, RF-05, RF-06).
  - Decidir el fin de la ronda y de la partida con game_logic.py (DF3) y enviar el resultado (RF-07 a RF-11).

Mensajes que enviará el servidor a los clientes:
  ROL|ronda|pacman        al comenzar cada ronda
  ESTADO|pos|puntos|tiempo   después de procesar cada jugada
  FIN_RONDA|puntos        al terminar una ronda (300 s o 4 fantasmas capturados)
  FIN_PARTIDA|ganador     al terminar las cinco rondas
"""
