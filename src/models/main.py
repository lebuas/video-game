import random
import sys
import time
import pygame
from mapa import Mapa
from personaje import Personaje
from enemigo import Enemigo  # Importamos la clase Enemigo
from combate import Combate
from explosion import Explosion

# Función para generar enemigos aleatorios


def generar_enemigo_aleatorio(ancho, alto, enemigos, enemigo_imgs):
    """Genera un enemigo aleatorio de tipo aleatorio y lo agrega a la lista de enemigos."""
    x = random.randint(0, ancho - 100)  # Posición aleatoria en el eje X
    y = random.randint(50, alto // 2)   # Posición aleatoria en el eje Y

    # Elegir aleatoriamente un tipo de enemigo (Nivel 1, Nivel 2 o Nivel 3)
    enemigo_tipo = random.choice([1, 2, 3])
    # Selecciona la imagen correspondiente
    enemigo_img = enemigo_imgs[enemigo_tipo]

    # Crear el enemigo con la imagen seleccionada
    enemigo = Enemigo(x, y, enemigo_img, 0, ancho, 0, alto // 2)
    enemigos.append(enemigo)


def mostrar_mensaje(screen, mensaje, font, color, posicion):
    """Función para mostrar un mensaje de texto en la pantalla."""
    texto = font.render(mensaje, True, color)
    screen.blit(texto, posicion)


def menu_fin_de_juego(screen, tiempo, victoria=True):
    """Muestra el menú de fin de juego con opciones de reintentar o salir."""
    font = pygame.font.Font(None, 50)
    color = (255, 255, 255)

    if victoria:
        mensaje = f"¡GANASTE! Tiempo: {int(tiempo)} segundos"
        opciones = ["Reintentar", "Salir"]
    else:
        mensaje = f"Perdiste. Tiempo: {int(tiempo)} segundos"
        opciones = ["Continuar", "Salir"]

    # Mostrar mensaje de victoria o derrota
    mostrar_mensaje(screen, mensaje, font, color, (400, 300))

    # Mostrar opciones
    for i, opcion in enumerate(opciones):
        mostrar_mensaje(screen, opcion, font, color, (400, 400 + i * 60))

    pygame.display.flip()

    # Manejar la entrada del jugador para reintentar o salir
    run_menu = True
    while run_menu:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return "salir"
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:  # Seleccionar arriba
                    return "reintentar" if victoria else "continuar"
                if evento.key == pygame.K_DOWN:  # Seleccionar abajo
                    return "salir"
                if evento.key == pygame.K_RETURN:  # Seleccionar la opción
                    return "reintentar" if victoria else "continuar"


def main():
    # Inicializar Pygame
    pygame.init()

    # Dimensiones de la ventana
    ancho, alto = 1200, 800

    # Rutas relativas de las imágenes (ajustadas)
    ruta_fondo = "../assets/images/map/fondo.png"
    tienda_img = "../assets/images/shops/tienda.png"
    recompensa_img = "../assets/images/map/recompensa.png"
    vidas_img = "../assets/images/map/vida.png"
    personaje_img = "../assets/images/player/personaje_n1.png"
    proyectil_img = "../assets/images/weapons/bala.png"
    proyectil_img_enemigo = "../assets/images/weapons/bala_enemigo.png"
    imagen_explosion_personaje = "../assets/images/effects/humo_n3.png"
    imagen_explosion_enemigo = "../assets/images/effects/explosion.png"
    imagen_explosion_balas = "../assets/images/effects/humo_n1.png"

    # Rutas de las imágenes de los enemigos (3 tipos)
    enemigo_imgs = {
        1: "../assets/images/enemies/enemigo_n1.png",  # Enemigo Nivel 1
        2: "../assets/images/enemies/enemigo_n2.png",  # Enemigo Nivel 2
        3: "../assets/images/enemies/enemigo_n3.png",  # Enemigo Nivel 3
    }

    # Crear una instancia del personaje
    enemigos = []
    proyectiles_pesonaje = []
    proyectiles_enemigo = []
    contador_bajas = 0
    contador_vida = 5
    tramapas = []

    # Objetos
    mapa = Mapa(ancho, alto, ruta_fondo, tienda_img, recompensa_img, vidas_img)
    personaje = Personaje(400, alto - 100, personaje_img,
                          contador_vida, contador_bajas)
    combate = Combate(personaje, enemigos,
                      proyectiles_pesonaje, proyectiles_enemigo, tramapas)

    # Generar el primer enemigo antes de entrar en el bucle
    generar_enemigo_aleatorio(ancho, alto, enemigos, enemigo_imgs)
    mapa.configurar_mapa()

    # Guardamos el tiempo de la última generación de enemigo
    last_enemy_time = time.time()

    # Inicializamos el reloj
    start_time = time.time()  # El tiempo al inicio del juego
    run_game = True

    while run_game:
        # Calculamos el tiempo transcurrido
        elapsed_time = time.time() - start_time  # Tiempo en segundos desde el inicio

        # Dibujar el fondo del mapa primero
        mapa.dibujar_mapa(contador_vida, contador_bajas, elapsed_time)

        # Controlar la generación de enemigos cada 3 segundos
        current_time = time.time()  # Obtenemos el tiempo actual
        if current_time - last_enemy_time >= 3:
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
            personaje.disparar(proyectiles_pesonaje, proyectil_img)

        # Mover los proyectiles del personaje
        for proyectil in proyectiles_pesonaje[:]:
            proyectil.mover()
            if proyectil.y < 0:  # El proyectil ha salido de la pantalla
                proyectiles_pesonaje.remove(proyectil)

        # Mover los proyectiles enemigos
        for proyectil in proyectiles_enemigo:
            proyectil.mover()
            if proyectil.y < 0:  # El proyectil ha salido de la pantalla
                proyectiles_enemigo.remove(proyectil)

        # Mover los enemigos y hacer que disparen
        for enemigo in enemigos:
            enemigo.mover()
            enemigo.actualizar_disparo(
                proyectiles_enemigo, proyectil_img_enemigo)

        # Dibujar el mapa y los objetos
        personaje.dibujar(mapa.screen)  # Dibujar el personaje después
        for enemigo in enemigos:       # Dibujar todos los enemigos
            enemigo.dibujar(mapa.screen)

        # Dibujar los proyectiles
        for proyectil_personaje in proyectiles_pesonaje:
            proyectil_personaje.dibujar(mapa.screen)

        for proyectil_enemigo in proyectiles_enemigo:
            proyectil_enemigo.dibujar(mapa.screen)

        # Comprobar colisiones y generar explosiones
        resultados_colision = combate.chequear_colisiones()

        for resultado in resultados_colision:
            coordenadas = resultado["coordenadas"]
            tipo = resultado["tipo"]

            # Determinar la imagen según el tipo de colisión
            if tipo == "impacto personaje":
                imagen_explosion = imagen_explosion_personaje
                contador_vida -= 1
            elif tipo == "impacto enemigo":
                contador_bajas += 1
                imagen_explosion = imagen_explosion_enemigo
            elif tipo == "impacto entre balas":
                imagen_explosion = imagen_explosion_balas

            # Crear y añadir la explosión
            nueva_explosion = Explosion.generar(coordenadas, imagen_explosion)
            combate.explosiones.append(nueva_explosion)

        # Dibujar y manejar explosiones
        for explosion in combate.explosiones[:]:
            explosion.dibujar(mapa.screen)
            if explosion.ha_terminado():
                combate.explosiones.remove(explosion)

        if personaje.verificar_progreso():
            resultado = menu_fin_de_juego(
                mapa.screen, elapsed_time, victoria=True)
            if resultado == "salir":
                break
            elif resultado == "reintentar":
                main()  # Reiniciar el juego
                return

        if contador_vida <= 0:  # Si pierde
            resultado = menu_fin_de_juego(
                mapa.screen, elapsed_time, victoria=False)
            if resultado == "salir":
                break
            elif resultado == "continuar":
                main()  # Continuar el juego (reiniciar)
                return

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar FPS
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
