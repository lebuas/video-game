import pygame


class Recompensa:
    def __init__(self, x, y):
        """Inicia una recompensa en la posición del enemigo destruido."""
        self.x = x
        self.y = y
        self.imagen = pygame.image.load(
            "path_to_star_image.png")  # Ruta de la estrella
        self.imagen = pygame.transform.scale(
            self.imagen, (50, 50))  # Ajuste de tamaño
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)

    def dibujar(self, screen):
        """Dibuja la recompensa (estrella) en la pantalla."""
        screen.blit(self.imagen, self.rect)
