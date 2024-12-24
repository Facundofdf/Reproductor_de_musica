import pygame
from boton import *
from funciones import *
#import json

def inicializar_ventana():
    """Esta funcion es la encargada de inicializar la ventanada del juego.

    Returns:
        _type_: La ventana principal y el fondo.
    """
    ANCHO_VENTANA = 800
    ALTO_VENTANA = 400

    pygame.init()
    pygame.mixer.init()

    ventana_ppal = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    
    pygame.display.set_caption("Reproductor de musica")
    
    icono = pygame.image.load(r"IMG\lisa.gif")
    pygame.display.set_icon(icono)

    fondo = pygame.image.load(r"IMG\fondo.png")
    fondo = pygame.transform.scale(fondo,(ANCHO_VENTANA, ALTO_VENTANA))

    return ventana_ppal, fondo

def crear_botones(ventana_ppal) -> list:
    """Esta funcion es la encargada de crear botones llamando a la funcion crear_boton.

    Args:
        ventana_ppal (_type_): La surface de la aplicacion.

    Returns:
        list: La lista de botones.
    """
    boton_play = crear_boton((50,50), (65,220), ventana_ppal,reproducir_musica, r"IMG\play.png")
    boton_pause = crear_boton((50,50), (165,220), ventana_ppal,pausar_musica, r"IMG\pause2.png")
    boton_stop = crear_boton((50,50), (265,220), ventana_ppal,detener_musica, r"IMG\stop.png")
    boton_up = crear_boton((50,50), (365,220), ventana_ppal,subir_volumen, r"IMG\up.png")
    boton_down = crear_boton((50,50), (465,220), ventana_ppal,bajar_volumen, r"IMG\down.png")
    boton_mute = crear_boton((50,50), (565,220), ventana_ppal,mutear, r"IMG\mute.png")
    boton_unmute = crear_boton((50,50), (665,220), ventana_ppal,desmutear, r"IMG\unmute.png")
    boton_siguiente = crear_boton((50,50), (410,280), ventana_ppal, siguiente_cancion, r"IMG\siguiente.png")
    boton_anterior = crear_boton((50,50), (330,280), ventana_ppal, anterior_cancion, r"IMG\anterior.png")

    lista = [boton_play, boton_pause, boton_stop, boton_up, boton_down, boton_mute, boton_unmute, boton_siguiente, boton_anterior]
    
    return lista

#def crear_botones_dinamicos(ventana_ppal):
#    lista = []
#    dimension = (50,50)
#    paths = [r"IMG\play.png", r"IMG\pause2.png", r"IMG\stop.png",r"IMG\up.png", r"IMG\down.png", r"IMG\mute.png",r"IMG\unmute.png" ]
#    posicion_inicial = [65,220]
#    acciones = ["reproducir_musica","pausar_musica","detener_musica","subir_volumen","bajar_volumen","mutear","desmutear"]
#    i = 0
#    for accion in acciones:
#        funcion = globals()[accion]
#        boton = crear_boton(dimension, posicion_inicial, ventana_ppal, funcion, paths[i])
#        lista.append(boton)
#        posicion_inicial = [posicion_inicial[0] + 100, posicion_inicial[1]]
#        i += 1
#    return lista
#
#def crear_botones_dinamicos_json(ventana_ppal):
#    lista = []
#
#    with open("config_botones.json", "r") as archivo:
#        config = json.load(archivo)
#    
#    tamaño = (config["ancho"], config["alto"])
#    posicion_inicial = config["posicion_inicial"]
#    i = 0
#
#    for accion in config["acciones"]:
#        funcion = globals()[accion]
#        boton = crear_boton(tamaño, posicion_inicial, ventana_ppal, funcion, config["paths"][i])
#        lista.append(boton)
#        posicion_inicial = [posicion_inicial[0] + 100, posicion_inicial[1]]
#        i += 1
#    return lista