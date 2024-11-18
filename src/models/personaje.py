
import pygame
import sys


class Personaje:
    def __init__(self, x, y, imagen):
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

    def mover(self, direccion):
        """
        Mueve al personaje a la izquierda o a la derecha.
        :param direccion: 'izquierda' o 'derecha'
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

    def dibujar(self, screen):
        """
        Dibuja al personaje en la pantalla.
        :param screen: Superficie en la que se va a dibujar el personaje.
        """
        screen.blit(self.imagen, self.rect)
