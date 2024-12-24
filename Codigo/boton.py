import pygame

def crear_boton(dimensiones, posicion, ventana, accion,  imagen: str = None) -> dict:
    """Esta funcion crea el diccionario con las caracteristicas necesarias para crear el boton.

    Args:
        dimensiones (_type_): Dimensiones del boton.
        posicion (_type_): La posicion en la pantalla.
        ventana (_type_): La surface.
        accion (_type_): La accion del boton.
        imagen (str, optional): El path de la imagen. Defaults to None.

    Returns:
        dict: El diccionario con las caracteristicas para crear el boton.
    """
    boton = {}
    boton["Ventana"] = ventana
    boton["Dimensiones"] = dimensiones
    boton["Posicion"] = posicion
    boton["Presionado"] = False
    boton["Accion"] = accion

    
    if imagen != None:
        img = pygame.image.load(imagen)
        boton["Contenido"] = pygame.transform.scale(img, boton["Dimensiones"]) 

    boton["Rectangulo"] = boton["Contenido"].get_rect()
    boton["Rectangulo"].topleft = boton["Posicion"]

    return boton

def dibujar(boton: dict):
    """Esta funcion dibuja el boton.

    Args:
        boton (dict): El diccionario del boton.
    """
    boton["Ventana"].blit(boton["Contenido"], boton["Posicion"])

def dibujar_botones(lista_botones: list):
    """Esta funcion es la encargada de dibujar una lista de botones,
    llamando a la funcion "dibujar".

    Args:
        lista (list): La lista de botones.
    """
    for boton in lista_botones:
        dibujar(boton)

def checkear_accion_botones(lista_botones: list, evento):
    """Esta funciones chekea la accion de los botones.

    Args:
        lista_botones (list): La lista de botones.
        evento (_type_): El evento de la aplicacion.
    """
    for boton in lista_botones:
        if boton["Rectangulo"].collidepoint(evento.pos):
            boton["Accion"]()
