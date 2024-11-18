import pygame


class Proyectil:
    def __init__(self, x, y):
        """
        Crea el proyectil que disparará el personaje.
        :param x: Posición inicial horizontal del proyectil
        :param y: Posición inicial vertical del proyectil
        """
        self.x = x
        self.y = y
        self.velocidad = 10  # Velocidad del proyectil
        self.radio = 5  # Tamaño del proyectil

    def mover(self):
        """
        Mueve el proyectil hacia arriba.
        """
        self.y -= self.velocidad

    def dibujar(self, screen):
        """
        Dibuja el proyectil en la pantalla.
        :param screen: Superficie en la que se va a dibujar el proyectil.
        """
        pygame.draw.circle(screen, (255, 0, 0), (self.x, self.y), self.radio)
