import pygame
import sys


class Mapa:
    def __init__(self, ancho, alto, fondo, tienda_img, recompensa_img, vidas_img):
        """
        Clase para configurar y renderizar el mapa.
        """
        self.ancho = ancho
        self.alto = alto
        try:
            # Fondo
            self.fondo = pygame.image.load(fondo)
            self.fondo = pygame.transform.scale(self.fondo, (ancho, alto))

            # Tienda
            self.tienda = pygame.image.load(tienda_img)
            self.tienda = pygame.transform.scale(self.tienda, (150, 150))

            # Mostrador de recompensa
            self.recompensa = pygame.image.load(recompensa_img)
            self.recompensa = pygame.transform.scale(self.recompensa, (70, 50))

            # Mostrador de vidas
            self.vidas = pygame.image.load(vidas_img)
            self.vidas = pygame.transform.scale(self.vidas, (50, 50))

        except pygame.error as e:
            print(f"Error al cargar las imágenes: {e}")
            sys.exit()

    def configurar_mapa(self):
        # Inicialización de Pygame
        pygame.init()

        # Configuración de la ventana
        self.screen = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Mapa con Objetos")

    def dibujar_mapa(self, vidas, recompensas, tiempo_restante):
        # Dibujar el fondo
        self.screen.blit(self.fondo, (0, 0))

        # Dibujar la tienda
        self.screen.blit(self.tienda, (0, 660))

        # Dibujar el mostrador de recompensa
        self.screen.blit(self.recompensa, (2, 10))

        # Dibujar el mostrador de vidas
        self.screen.blit(self.vidas, (1150, 755))

        # Mostrar el número de vidas
        font = pygame.font.Font(None, 36)
        vidas_text = font.render(f"{vidas}", True, (255, 255, 255))
        self.screen.blit(vidas_text, (1168, 747))

        # Mostrar el número de recompensas
        recompensas_text = font.render(
            f"{recompensas}", True, (255, 255, 255))
        self.screen.blit(recompensas_text, (31.5, 55))

        # Mostrar el tiempo restante
        tiempo_text = font.render(
            f"Tiempo: {int(tiempo_restante)}", True, (187, 26, 160))
        self.screen.blit(tiempo_text, (1000, 10))
