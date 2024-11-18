import pygame
import random
import sys
from mapa import Mapa
from personaje import Personaje
from proyectil import Proyectil
from enemigo import Enemigo  # Importamos la clase Enemigo


def main():
    # Dimensiones de la ventana
    ancho, alto = 1200, 800

    # Rutas relativas de las imágenes (ajustadas)
    ruta_fondo = "../assets/images/map/fondo.png"
    tienda_img = "../assets/images/shops//tienda.png"
    recompensa_img = "../assets/images/map/recompensa.png"
    vidas_img = "../assets/images/map/vida.png"
    personaje_img = "../assets/images/player/personaje_n1.png"
    enemigo_img = "../assets/images/enemies/enemigo_n1.png"  # Imagen del enemigo

    # Crear una instancia del mapa
    mapa = Mapa(ancho, alto, ruta_fondo, tienda_img, recompensa_img, vidas_img)

    # Crear una instancia del personaje
    personaje = Personaje(400, alto - 100, personaje_img)

    # Crear una instancia del enemigo
    # Los límites de movimiento están definidos de la siguiente forma:
    # - Se mueve de izquierda a derecha entre 0 y 1200
    # - Se mueve de arriba hacia abajo entre 0 y 400
    enemigo = Enemigo(random.randint(0, ancho - 100), random.randint(50,
                      alto // 2), enemigo_img, 0, ancho, 0, alto // 2)

    # Lista de proyectiles
    proyectiles = []

    mapa.configurar_mapa()

    # Bucle principal
    run_game = True
    while run_game:
        mapa.dibujar_mapa()  # Dibujar el fondo del mapa primero

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                run_game = False

        # Movimiento del personaje
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:  # Mover a la izquierda
            personaje.mover('izquierda')
        if teclas[pygame.K_RIGHT]:  # Mover a la derecha
            personaje.mover('derecha')

        # Disparo con la tecla Espacio
        if teclas[pygame.K_SPACE]:
            # Crear un proyectil en la posición del personaje
            proyectil = Proyectil(
                personaje.x + personaje.rect.width // 2, personaje.y)
            proyectiles.append(proyectil)

        # Mover los proyectiles
        for proyectil in proyectiles[:]:
            proyectil.mover()
            if proyectil.y < 0:  # El proyectil ha salido de la pantalla
                proyectiles.remove(proyectil)

        # Mover al enemigo
        enemigo.mover()

        # Dibujar el mapa y los objetos
        personaje.dibujar(mapa.screen)  # Dibujar el personaje después
        enemigo.dibujar(mapa.screen)  # Dibujar el enemigo

        # Dibujar los proyectiles
        for proyectil in proyectiles:
            proyectil.dibujar(mapa.screen)

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar FPS
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
