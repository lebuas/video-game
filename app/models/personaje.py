
import time
import pygame
from proyectil import Proyectil


class Personaje:
    def __init__(self, x, y, imagen, vida, bajas):
        """
        Inicializa el personaje.
        :param x: Posición horizontal
        :param y: Posición vertical
        :param imagen: Ruta de la imagen del personaje
        """
        self.x = x
        self.y = y
        self.imagen = pygame.image.load(imagen)  # Cargar la imagen
        self.imagen = pygame.transform.scale(self.imagen, (100, 100))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        self.velocidad = 8  # Velocidad de movimiento
        self.last_shot_time = 0  # Tiempo del último disparo
        self.shot_delay = 0.3  # 300 milisegundos entre disparos
        self.vida = vida
        self.kills = bajas

    def mover(self, direccion):
        """
        Mueve al personaje a la izquierda o a la derecha.
        """
        if direccion == 'izquierda':
            self.x -= self.velocidad
        elif direccion == 'derecha':
            self.x += self.velocidad

        # Limitar el movimiento dentro de los bordes de la pantalla
        if self.x < 0:
            self.x = 0
        elif self.x + self.rect.width > 1200:
            self.x = 1200 - self.rect.width

        self.rect.topleft = (self.x, self.y)

    def disparar(self, proyectiles, proyectil_img):
        """
        Maneja el disparo de proyectiles desde la posición del personaje.
        proyectiles: Lista de proyectiles actuales en el juego.
        proyectil_img: Ruta de la imagen del proyectil.
        """
        # Comprobamos si el tiempo entre disparos ha pasado
        if time.time() - self.last_shot_time >= self.shot_delay:
            # Crear un proyectil en la posición del personaje
            proyectil = Proyectil(
                self.x-5 + self.rect.width // 2, self.y, proyectil_img)
            proyectiles.append(proyectil)
            self.last_shot_time = time.time()  # Actualizamos el tiempo del último disparo

    # Aqui se controla la victoria o derrota
    def verificar_progreso(self, tiempo):
        if self.vida < 5:
            return False
        elif self.kills >= 5 and tiempo <= 60:
            return True

    def dibujar(self, screen):
        """
        Dibuja al personaje en la pantalla.
        """
        screen.blit(self.imagen, self.rect)
