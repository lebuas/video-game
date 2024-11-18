
import pygame
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
        self.imagen = pygame.image.load(imagen)  # Cargar la imagen del enemigo
        self.imagen = pygame.transform.scale(
            self.imagen, (100, 100))  # Ajustar el tamaño
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        self.velocidad_x = 8  # Velocidad de movimiento en el eje X
        self.velocidad_y = 4  # Velocidad de movimiento en el eje Y
        # Dirección aleatoria horizontal (izquierda o derecha)
        self.direccion_x = random.choice([-1, 1])
        # Dirección aleatoria vertical (arriba o abajo)
        self.direccion_y = random.choice([-1, 1])

        # Límites de movimiento
        self.limite_izquierda = limite_izquierda
        self.limite_derecha = limite_derecha
        self.limite_arriba = limite_arriba
        self.limite_abajo = limite_abajo

    def mover(self):
        """
        Mueve al enemigo dentro del área definida.
        El enemigo puede moverse horizontal y verticalmente.
        """
        # Movimiento horizontal
        self.x += self.velocidad_x * self.direccion_x
        if self.x <= self.limite_izquierda or self.x + self.rect.width >= self.limite_derecha:
            self.direccion_x *= -1  # Cambiar dirección horizontal

        # Movimiento vertical
        self.y += self.velocidad_y * self.direccion_y
        if self.y <= self.limite_arriba or self.y + self.rect.height >= self.limite_abajo:
            self.direccion_y *= -1  # Cambiar dirección vertical

        self.rect.topleft = (self.x, self.y)

    def dibujar(self, screen):
        """
        Dibuja al enemigo en la pantalla.
        :param screen: Superficie en la que se va a dibujar el enemigo.
        """
        screen.blit(self.imagen, self.rect)
