import pygame
from boton import *
from funciones import *
from configuraciones import *

def manejador_eventos(lista_botones: list) -> bool:
    """Esta funcion es la encargada de manejar eventos,
    dependiendo del valor de la bandera.

    Args:
        lista_botones (list): La lista de botones.

    Returns:
        bool: La bandera que maneja los eventos.
    """
    flag_run = True
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_run = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            checkear_accion_botones(lista_botones, evento)

    return flag_run

def main_reproductor():
    """Esta funcion es la encargada de ejecutar la aplicacion.
    """

    ventana_ppal, fondo = inicializar_ventana()

    lista = crear_botones(ventana_ppal)
    # lista = crear_botones_dinamicos(ventana_ppal)
    #lista = crear_botones_dinamicos_json(ventana_ppal)

    cargar_musica(playlist[current_song_index])
    reproducir_musica()

    flag_run = True

    while flag_run:
        flag_run = manejador_eventos(lista)

        ventana_ppal.blit(fondo,(0,0))
        dibujar_botones(lista)

        pygame.display.update()

    pygame.quit()

main_reproductor()