
import pygame


class Proyectil:
    def __init__(self, x, y, imagen, velocidad=10, direccion_y=-1):
        """
        Crea el proyectil.
        :param x: Posición inicial horizontal
        :param y: Posición inicial vertical
        :param imagen: Ruta de la imagen del proyectil
        :param velocidad: Velocidad de movimiento del proyectil
        :param direccion_y: Dirección de movimiento en el eje Y (-1 para arriba, 1 para abajo)
        """
        self.x = x
        self.y = y
        self.velocidad = velocidad
        self.direccion_y = direccion_y  # Dirección de movimiento vertical
        # Cargar la imagen del proyectil
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(
            self.imagen, (8, 15))  # Ajusta el tamaño de la imagen
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)

    def mover(self):
        """Mueve el proyectil en la dirección vertical definida."""
        self.y += self.velocidad * self.direccion_y
        self.rect.topleft = (self.x, self.y)

    def dibujar(self, screen):
        """Dibuja el proyectil en la pantalla."""
        screen.blit(self.imagen, self.rect)
