import time
import pygame
from proyectil import Proyectil
import random


class Enemigo:
    def __init__(self, x, y, imagen, limite_izquierda, limite_derecha, limite_arriba, limite_abajo):
        """
        Inicializa el enemigo.
        :param x: Posición inicial horizontal
        :param y: Posición inicial vertical
        :param imagen: Ruta de la imagen del enemigo
        :param limite_izquierda: El límite izquierdo de movimiento
        :param limite_derecha: El límite derecho de movimiento
        :param limite_arriba: El límite superior de movimiento
        :param limite_abajo: El límite inferior de movimiento
        """
        self.x = x
        self.y = y
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, (100, 100))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        self.velocidad_x = 8
        self.velocidad_y = 4
        self.direccion_x = random.choice([-1, 1])
        self.direccion_y = random.choice([-1, 1])

        # Límites de movimiento
        self.limite_izquierda = limite_izquierda
        self.limite_derecha = limite_derecha
        self.limite_arriba = limite_arriba
        self.limite_abajo = limite_abajo

        # Controlar el tiempo de disparo
        self.last_shot_time = time.time()
        # Intervalo de disparo en segundos (puedes ajustarlo)
        self.shot_interval = 1

    def mover(self):
        """Mueve al enemigo dentro del área definida."""
        if self.x <= self.limite_izquierda or self.x + self.rect.width >= self.limite_derecha:
            self.direccion_x *= -1

        if self.y <= self.limite_arriba or self.y + self.rect.height >= self.limite_abajo:
            self.direccion_y *= -1

        self.x += self.velocidad_x * self.direccion_x
        self.y += self.velocidad_y * self.direccion_y

        self.x = max(self.limite_izquierda, min(
            self.x, self.limite_derecha - self.rect.width))
        self.y = max(self.limite_arriba, min(
            self.y, self.limite_abajo - self.rect.height))

        self.rect.topleft = (self.x, self.y)

    def disparar(self, imagen_proyectil):
        """Dispara un proyectil hacia abajo."""
        proyectil = Proyectil(self.x + self.rect.width // 2, self.y +
                              self.rect.height, imagen_proyectil, direccion_y=1)
        return proyectil

    def actualizar_disparo(self, proyectiles, imagen_proyectil):
        """Controla el disparo del enemigo y lo actualiza si es el momento adecuado."""
        current_time = time.time()

        # Verificar si ha pasado el intervalo desde el último disparo
        if current_time - self.last_shot_time >= self.shot_interval:
            # Disparar un proyectil
            proyectil = self.disparar(imagen_proyectil)
            proyectiles.append(proyectil)
            self.last_shot_time = current_time  # Actualizar el tiempo del último disparo

    def dibujar(self, screen):
        """Dibuja al enemigo en la pantalla."""
        screen.blit(self.imagen, self.rect)
