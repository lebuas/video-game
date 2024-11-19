import pygame
import random
import sys
import time
from mapa import Mapa
from personaje import Personaje
from proyectil import Proyectil
from enemigo import Enemigo  # Importamos la clase Enemigo

# Función para generar enemigos aleatorios


def generar_enemigo_aleatorio(ancho, alto, enemigos, enemigo_imgs):
    """Genera un enemigo aleatorio de tipo aleatorio y lo agrega a la lista de enemigos."""
    x = random.randint(0, ancho - 100)  # Posición aleatoria en el eje X
    y = random.randint(50, alto // 2)   # Posición aleatoria en el eje Y

    # Elegir aleatoriamente un tipo de enemigo (Nivel 1, Nivel 2 o Nivel 3)
    # Elige un tipo de enemigo aleatorio
    enemigo_tipo = random.choice([1, 2, 3])
    # Selecciona la imagen correspondiente
    enemigo_img = enemigo_imgs[enemigo_tipo]

    # Crear el enemigo con la imagen seleccionada
    enemigo = Enemigo(x, y, enemigo_img, 0, ancho, 0, alto // 2)
    enemigos.append(enemigo)


def main():
    # Dimensiones de la ventana
    ancho, alto = 1200, 800

    # Rutas relativas de las imágenes (ajustadas)
    ruta_fondo = "../assets/images/map/fondo.png"
    tienda_img = "../assets/images/shops//tienda.png"
    recompensa_img = "../assets/images/map/recompensa.png"
    vidas_img = "../assets/images/map/vida.png"
    personaje_img = "../assets/images/player/personaje_n1.png"

    # Rutas de las imágenes de los enemigos (3 tipos)
    enemigo_imgs = {
        1: "../assets/images/enemies/enemigo_n1.png",  # Enemigo Nivel 1
        2: "../assets/images/enemies/enemigo_n2.png",  # Enemigo Nivel 2
        3: "../assets/images/enemies/enemigo_n3.png",  # Enemigo Nivel 3
    }

    # Crear una instancia del mapa
    mapa = Mapa(ancho, alto, ruta_fondo, tienda_img, recompensa_img, vidas_img)

    # Crear una instancia del personaje
    personaje = Personaje(400, alto - 100, personaje_img)

    # Lista de enemigos
    enemigos = []

    # Generar el primer enemigo antes de entrar en el bucle
    generar_enemigo_aleatorio(ancho, alto, enemigos, enemigo_imgs)

    # Lista de proyectiles
    proyectiles = []

    mapa.configurar_mapa()

    # Guardamos el tiempo de la última generación de enemigo
    last_enemy_time = time.time()
    run_game = True
    while run_game:
        mapa.dibujar_mapa(3, 0, 120)  # Dibujar el fondo del mapa primero

        # Controlar la generación de enemigos cada 10 segundos
        current_time = time.time()  # Obtenemos el tiempo actual
        if current_time - last_enemy_time >= 10:  # Si han pasado 10 segundos
            generar_enemigo_aleatorio(ancho, alto, enemigos, enemigo_imgs)
            last_enemy_time = current_time  # Actualizamos el tiempo de la última generación

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

        # Mover los enemigos
        for enemigo in enemigos:
            enemigo.mover()

        # Dibujar el mapa y los objetos
        personaje.dibujar(mapa.screen)  # Dibujar el personaje después
        for enemigo in enemigos:       # Dibujar todos los enemigos
            enemigo.dibujar(mapa.screen)

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
