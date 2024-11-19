
import pygame
import time


class Explosion:
    def __init__(self, x, y, imagen_explosion, duracion=0.1):
        """
        Crea una nueva explosión en las coordenadas dadas.

        :param x: Coordenada X de la explosión.
        :param y: Coordenada Y de la explosión.
        :param imagen_explosion: Ruta de la imagen de explosión.
        :param duracion: Duración de la explosión en segundos (por defecto: 2).
        """
        self.x = x
        self.y = y
        self.imagen = pygame.image.load(imagen_explosion)
        self.imagen = pygame.transform.scale(self.imagen, (100, 100))
        self.rect = self.imagen.get_rect(center=(x, y))
        self.inicio = time.time()  # Marca el momento en que se crea la explosión
        self.duracion = duracion

    def dibujar(self, pantalla):
        """Dibuja la explosión en la pantalla."""
        pantalla.blit(self.imagen, self.rect)

    def ha_terminado(self):
        """Devuelve True si la explosión ha durado más del tiempo permitido."""
        return time.time() - self.inicio >= self.duracion

    @staticmethod
    def generar(coordenadas, imagen_explosion, duracion=0.1):
        """
        Método estático para crear una nueva explosión.

        :param coordenadas: (x, y) Coordenadas de la explosión.
        :param imagen_explosion: Ruta de la imagen de la explosión.
        :param duracion: Duración de la explosión en segundos.
        :return: Una instancia de la clase Explosion.
        """
        x, y = coordenadas
        return Explosion(x, y, imagen_explosion, duracion)
