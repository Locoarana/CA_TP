import os
import keyboard
from colorama import Fore
from colorama import Style
from pynput.keyboard import Key, Listener


def limpiar_pantalla():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system("cls")


def juego():
    # datos del mapa
    filas = 9
    columnas = 9

    # caracteres para identificar los elementos dentro del mapa
    casilla_libre = 'c'
    char_bot = 'b'
    char_jugador = 'j'

    # coordenadas del bot y el jugador
    bot_coords = [0, round(columnas / 2)]
    jugador_coords = [filas - 1, round(columnas / 2)]

    # creacion del mapa inicial
    mapa = [[casilla_libre for y in range(columnas)] for x in range(filas)]

    # dibujamos al bot y al jugador en el mapa
    mapa[bot_coords[0]][bot_coords[1]] = char_bot
    mapa[jugador_coords[0]][jugador_coords[1]] = char_jugador

    def mover_jugador(movimiento):
        mapa[jugador_coords[0]][jugador_coords[1]] = casilla_libre
        if movimiento == "arriba":
            jugador_coords[0] = jugador_coords[0] - 1
            dibujar_jugador()
        elif movimiento == "abajo":
            jugador_coords[0] = jugador_coords[0] + 1
            dibujar_jugador()
        elif movimiento == "derecha":
            jugador_coords[1] = jugador_coords[1] + 1
            dibujar_jugador()
        elif movimiento == "izquierda":
            jugador_coords[1] = jugador_coords[1] - 1
            dibujar_jugador()

    def es_movimiento_valido(x, y):
        res = (x >= 0) and (x < filas)
        res = res and (y >= 0) and (y < columnas)
        res = res and (mapa[x][y] == casilla_libre)
        if not res:
            return False
        else:
            return True

    def dibujar_jugador():
        mapa[jugador_coords[0]][jugador_coords[1]] = char_jugador

    def dibujar_mapa():
        for i in range(filas):
            for j in range(columnas):
                if mapa[i][j] == casilla_libre:
                    print("x ", end="")
                elif mapa[i][j] == char_jugador:
                    print(f'{Fore.GREEN}x{Style.RESET_ALL} ', end="")
                elif mapa[i][j] == char_bot:
                    print(f'{Fore.RED}x{Style.RESET_ALL} ', end="")
                else:
                    print("- ", end="")
            print("\n", end="")

    limpiar_pantalla()
    dibujar_mapa()

    def on_press(key):
        if key == Key.esc:
            return False
        if str(key) == "'w'":
            if es_movimiento_valido(jugador_coords[0] - 1, jugador_coords[1]):
                limpiar_pantalla()
                mover_jugador("arriba")
                dibujar_mapa()

        if str(key) == "'s'":
            if es_movimiento_valido(jugador_coords[0] + 1, jugador_coords[1]):
                limpiar_pantalla()
                mover_jugador("abajo")
                dibujar_mapa()

        if str(key) == "'a'":
            if es_movimiento_valido(jugador_coords[0], jugador_coords[1] - 1):
                limpiar_pantalla()
                mover_jugador("izquierda")
                dibujar_mapa()

        if str(key) == "'d'":
            if es_movimiento_valido(jugador_coords[0], jugador_coords[1] + 1):
                limpiar_pantalla()
                mover_jugador("derecha")
                dibujar_mapa()

    with Listener(on_press=on_press) as listener:
        listener.join()


# Pantalla inicio
while True:
    limpiar_pantalla()
    print("Bienvenido!")
    print("Presione 'y' para iniciar el juego o ESC para salir...")
    if keyboard.read_key() == "y":
        print('Inicio el juego!')
        juego()
        break
    elif keyboard.read_key() == "esc":
        print("Finalizo el juego!")
        break
