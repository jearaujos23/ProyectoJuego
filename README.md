# Pac-Man multijugador competitivo

Proyecto integrador de **Lógica de Programación** · UIDE · Fase 3: Entorno de trabajo

- **Docente:** Harry Carpio
- **Paralelo:** C
- **Integrantes:** Joshua Garzón, Eduardo Araujo.

## El juego

Pac-Man multijugador competitivo para cinco participantes en red LAN (cliente-servidor): en cada ronda un jugador controla a Pac-Man y los otros cuatro controlan fantasmas. Cada ronda dura 300 segundos o termina cuando Pac-Man captura a los cuatro fantasmas. Los roles rotan en cada una de las cinco rondas y gana quien acumule más puntos.

**Estado en esta fase:** código inicial. Está traducido a Python el menú (DF1) y las decisiones de validar una jugada (DF2) y terminar la ronda (DF3). La partida completa y los sockets se programan en la Fase 4.

## Estructura del repositorio

```
ProyectoJuego/
├── juego.py         ← punto de entrada: menú que se repite hasta «Salir» (parte de DF1)
├── game_logic.py    ← validación de la jugada (DF2) y fin de la ronda / partida (DF3)
├── server.py        ← servidor, Jugador 1 (por ahora, un comentario)
├── client.py        ← cliente, Jugadores 2 a 5 (por ahora, un comentario)
├── diseno/          ← diagramas .rap de la Fase 2
├── LICENSE
└── README.md
```

## Cómo ejecutarlo

Requiere Python 3 (solo se usa la biblioteca estándar, no hay que instalar nada).

```
python juego.py
python game_logic.py
```

**Pruebas rápidas** (lo que se escribe en cada pregunta):

| Programa | Qué probar | Qué se espera |
|---|---|---|
| `juego.py` | `5` | «Opcion invalida: use 1 o 2» y vuelve a pedir la opción |
| `juego.py` | `1` y luego `2` | Mensaje de «Jugar» y después «Salir» |
| `game_logic.py` (DF2) | Jugador `1`, dirección `9` | «Error de formato: direccion invalida» y vuelve a pedir la jugada |
| `game_logic.py` (DF2) | Jugador `1`, dirección `1` | «Movimiento bloqueado: pared» (la pared está en 12,9) y vuelve a pedir la jugada |
| `game_logic.py` (DF2) | Jugador `1`, dirección `4` | «Movimiento aceptado» y posición resultante 13, 10 |
| `game_logic.py` (DF3) | Ronda `3`, `150` s, `2` capturados | «La ronda continua» |
| `game_logic.py` (DF3) | Ronda `3`, `0` s, `2` capturados | «FIN: se cumplieron los 300 segundos» y pasa a la ronda 4 |
| `game_logic.py` (DF3) | Ronda `5`, `0` s, `4` capturados y puntos `10 20 30 5 0` | «GANADOR: JUGADOR 3» con 30 puntos |
| `game_logic.py` (DF3) | Ronda `5`, `0` s, `4` capturados y puntos `10 20 20 5 0` | «EMPATE en primer lugar: desempate pendiente» |

## Del diagrama de la Fase 2 al código

| Diagrama de la Fase 2 | Archivo y líneas | Qué cambió |
|---|---|---|
| DF1 · Menú «1 Jugar / 2 Salir» (RF-01) | `juego.py`, líneas 13–32 | El `Loop` de RAPTOR pasó a un `while`. El `GET menu` es `input()`. Se lee texto, así que cualquier cosa distinta de 1 y 2 («5», «x») muestra «Opcion invalida: use 1 o 2». La opción «Jugar» solo muestra un mensaje; la partida completa va en la Fase 4. |
| DF2 · Validación de la jugada (RF-04, RF-05, RF-06) | `game_logic.py`, líneas 32–79 | Los `GET` pasaron a `input()` con una función que detecta si lo escrito no es un número (se trata como entrada inválida). Los `Selection` anidados pasaron a `if`. El estado de ejemplo (x = 12, y = 10, pared en 12,9, laberinto 25x21) se asigna al inicio de la función, como en RAPTOR. |
| DF3 · Fin de ronda, rotación y ganador (RF-07 a RF-11) | `game_logic.py`, líneas 85–171 | Los `GET` pasaron a `input()` con validación de rangos. Los `PUT` que mostraban el número en otra línea (ronda, jugador, ganador, total) siguen igual. Se mantienen las variables sueltas `p1` a `p5`, sin listas, como en el diagrama. |

## Video explicativo
https://1drv.ms/v/c/bd781ab2418f6cef/IQCPq1-J4dbsSJZ0Fm98Dai3AQ_i-EKKW0DYUQC2NhTsqBU?e=LO2ODz 

## Licencia

Este proyecto se publica bajo la licencia **MIT** (archivo `LICENSE`).

## Créditos y declaración de autoría

- **Autoría:** el diseño del juego, los requisitos y los diagramas RAPTOR de las Fases 1 y 2 son del equipo. El código de las Fases 3 en adelante se basa en esos diagramas.
- **Código de terceros:** ninguno. Solo se usa la biblioteca estándar de Python.
- **Librerías:** no hay librerías externas en esta fase.
- **Recursos visuales:** ninguno en esta fase.
- **Herramientas de IA:** se usó Claude para redactar el README y preparar el archivo de licencia. 
