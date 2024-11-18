import pygame
import sys


class Mapa:
    def __init__(self, ancho, alto, fondo, tienda_img, recompensa_img, vidas_img):
        """
        Clase para configurar y renderizar el mapa.
        ancho: Ancho de la ventana
        alto: Alto de la ventana
        fondo: Ruta de la imagen de fondo
        tienda_img: Ruta de la imagen de la tienda
        recompensa_img: Ruta de la imagen del mostrador de recompensa
        vidas_img: Ruta de la imagen del mostrador de vidas
        """
        self.ancho = ancho
        self.alto = alto
        try:
            # Fondo
            self.fondo = pygame.image.load(fondo)
            self.fondo = pygame.transform.scale(self.fondo, (ancho, alto))

            # Tienda
            self.tienda = pygame.image.load(tienda_img)
            self.tienda = pygame.transform.scale(
                self.tienda, (150, 150))  # Ajustar tamaño

            # Mostrador de recompensa
            self.recompensa = pygame.image.load(recompensa_img)
            self.recompensa = pygame.transform.scale(
                self.recompensa, (70, 50))  # Ajustar tamaño

            # Mostrador de vidas
            self.vidas = pygame.image.load(vidas_img)
            self.vidas = pygame.transform.scale(
                self.vidas, (50, 50))  # Ajustar tamaño

        except pygame.error as e:
            print(f"Error al cargar las imágenes: {e}")
            sys.exit()

    def configurar_mapa(self):
        # Inicialización de Pygame
        pygame.init()

        # Configuración de la ventana
        self.screen = pygame.display.set_mode((self.ancho, self.alto))
        pygame.display.set_caption("Mapa con Objetos")

    def dibujar_mapa(self):
        # Dibujar el fondo
        self.screen.blit(self.fondo, (0, 0))

        # Dibujar la tienda (esquina inferior izquierda)
        self.screen.blit(self.tienda, (0, 660))

        # Dibujar el mostrador de recompensa (alineado en la parte inferior)
        self.screen.blit(self.recompensa, (2, 10))

        # Dibujar el mostrador de vidas (alineado en la parte inferior)
        self.screen.blit(self.vidas, (1160, 755))
