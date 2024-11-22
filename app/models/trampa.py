
import pygame
import random


class Trampa:
    def __init__(self, x, y, nivel, imagen_trampa):
        """
        Crea una nueva trampa en las coordenadas dadas.

        x: Coordenada X de la trampa.
        y: Coordenada Y de la trampa.
        nivel: Nivel de la trampa (1, 2 o 3).
        imagen_trampa: Ruta de la imagen de la trampa.
        """
        self.x = x
        self.y = y
        self.nivel = nivel
        self.imagen = pygame.image.load(imagen_trampa)
        self.imagen = pygame.transform.scale(
            self.imagen, (50, 50))  # Escala ajustada
        self.rect = self.imagen.get_rect(center=(x, y))
        self.velocidad = random.randint(2, 5)  # Velocidad aleatoria de caída

    def mover(self):
        """Mueve la trampa hacia abajo."""
        self.y += self.velocidad
        self.rect.y = self.y

    def dibujar(self, pantalla):
        """Dibuja la trampa en la pantalla."""
        pantalla.blit(self.imagen, self.rect)

    def verificar_colision(self, personaje):
        """
        Verifica si la trampa colisiona con el personaje.

        :param personaje: Objeto del personaje.
        :return: Nivel de daño según el nivel de la trampa, o None si no hay colisión.
        """
        if self.rect.colliderect(personaje.rect):
            return self.nivel
        return None
