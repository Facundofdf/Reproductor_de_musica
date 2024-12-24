import pygame

playlist = ["Sonidos/Michael Bibi - Got The Fire.mp3", 
            "Sonidos/Dennis Cruz - Ready For The Blues.mp3", 
            "Sonidos/Josh Butler & Bontan - Call You Back.mp3"]
current_song_index = 0

def cargar_musica(playlist: list):
    """Esta funcion carga la musica.

    Args:
        playlist (list): La lista de canciones.
    """
    pygame.mixer.music.load(playlist)

def reproducir_musica():
    """Esta funcion reproduce la musica.
    """
    pygame.mixer.music.play()

def pausar_musica():
    """Esta funcion es para pausar la musica.
    """
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        reanudar_musica()

def reanudar_musica():
    """Esta funcion es para reanudar la musica.
    """
    pygame.mixer.music.unpause()

def detener_musica():
    """Esta funcion es para dar stop a la musica.
    """
    pygame.mixer.music.stop()

def mutear():
    """Esta funcion mutea la musica.
    """
    pygame.mixer.music.set_volume(0)

def desmutear():
    """Esta funcion desmutea la musica.
    """
    pygame.mixer.music.set_volume(0.3)

def subir_volumen():
    """Esta funcion sube el volumen de la musica.
    """
    actual = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(actual + 0.05)

def bajar_volumen():
    """Esta funcion baja el volumen de la musica.
    """
    actual = pygame.mixer.music.get_volume()
    pygame.mixer.music.set_volume(actual - 0.05)

def siguiente_cancion():
    """Esta funcion pasa a la siguiente cancion.
    """
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    cargar_musica(playlist[current_song_index])
    reproducir_musica()

def anterior_cancion():
    """Esta funcion vuelve a la cancion anterior.
    """
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist)
    cargar_musica(playlist[current_song_index])
    reproducir_musica()