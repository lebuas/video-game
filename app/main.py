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


# Función para mostrar el menú al final del juego
def mostrar_menu_final(screen, mensaje, tiempo, reintentar=True):
    fuente = pygame.font.SysFont("Arial", 36)
    texto_mensaje = fuente.render(mensaje, True, (255, 255, 255))
    texto_tiempo = fuente.render(
        f"Tiempo: {int(tiempo)} segundos", True, (255, 255, 255))

    # Posicionar el mensaje en el centro de la pantalla
    screen.fill((0, 0, 0))  # Fondo negro
    screen.blit(texto_mensaje, (screen.get_width() //
                2 - texto_mensaje.get_width() // 2, 200))
    screen.blit(texto_tiempo, (screen.get_width() //
                2 - texto_tiempo.get_width() // 2, 250))

    if reintentar:
        opcion_texto = fuente.render(
            "Presiona 'R' para reintentar o 'S' para salir.", True, (255, 255, 255))
    else:
        opcion_texto = fuente.render(
            "Presiona 'C' para continuar o 'S' para salir.", True, (255, 255, 255))

    screen.blit(opcion_texto, (screen.get_width() //
                2 - opcion_texto.get_width() // 2, 300))
    pygame.display.flip()


def main():
    # Inicializar Pygame
    pygame.init()

    # Dimensiones de la ventana
    ancho, alto = 1200, 800

    # Rutas relativas de las imágenes (ajustadas)
    ruta_fondo = "assets/map/fondo.png"
    tienda_img = "assets/shops/tienda.png"
    recompensa_img = "assets/map/recompensa.png"
    vidas_img = "assets/map/vida.png"
    personaje_img = "assets/player/personaje_n1.png"
    proyectil_img = "assets/weapons/bala.png"
    proyectil_img_enemigo = "assets/weapons/bala_enemigo.png"
    imagen_explosion_personaje = "assets/effects/humo_n3.png"
    imagen_explosion_enemigo = "assets/effects/explosion.png"
    imagen_explosion_balas = "assets/effects/humo_n1.png"

    # Rutas de las imágenes de los enemigos (3 tipos)
    enemigo_imgs = {
        1: "assets/enemies/enemigo_n1.png",  # Enemigo Nivel 1
        2: "assets/enemies/enemigo_n2.png",  # Enemigo Nivel 2
        3: "assets/enemies/enemigo_n3.png",  # Enemigo Nivel 3
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
    run_game = True
    tiempo_inicio = time.time()

    while run_game:
        # Dibujar el fondo del mapa primero
        elapsed_time = time.time() - tiempo_inicio
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
                contador_vida = contador_vida-1
            elif tipo == "impacto enemigo":
                contador_bajas = contador_bajas + 1
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
            # Mostrar mensaje de victoria
            mostrar_menu_final(mapa.screen, "¡Ganaste!",
                               time.time() - tiempo_inicio, reintentar=True)
            # Esperar la respuesta del jugador
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_r]:  # Reintentar
                main()
            elif tecla[pygame.K_s]:  # Salir
                run_game = False
        elif contador_vida <= 0:
            # Mostrar mensaje de derrota
            mostrar_menu_final(mapa.screen, "¡Perdiste!",
                               time.time() - tiempo_inicio, reintentar=False)
            # Esperar la respuesta del jugador
            tecla = pygame.key.get_pressed()
            if tecla[pygame.K_s]:  # Salir
                run_game = False
            elif tecla[pygame.K_r]:  # Reintentar
                main()

        # Actualizar la pantalla
        pygame.display.flip()

        # Controlar FPS
        pygame.time.Clock().tick(60)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
