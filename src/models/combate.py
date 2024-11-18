
import pygame
import sys


class Combate:
    def __init__(self, enemigo, proyectil, animacion_humo_img, estrella_img, personaje):
        self.enemigo = enemigo
        self.proyectil = proyectil
        self.animacion_humo_img = pygame.image.load(animacion_humo_img)
        self.animacion_humo_img = pygame.transform.scale(
            self.animacion_humo_img, (100, 100))
        self.humo_rect = self.animacion_humo_img.get_rect()
        self.estrella_img = pygame.image.load(estrella_img)
        self.estrella_img = pygame.transform.scale(self.estrella_img, (50, 50))
        self.estrella_rect = self.estrella_img.get_rect()

        self.colisionada = False  # Indica si el proyectil ha colisionado con el enemigo
        self.estrella_caida = False  # Indica si la estrella ya ha caído
        self.contador_estrellas = 0  # Contador de estrellas recogidas
        self.personaje = personaje  # El personaje principal
        self.vidas = 3  # Vidas del personaje
        # Posición de la estrella cuando el enemigo es destruido
        self.estrella_pos = (0, 0)

    def chequear_colision(self):
        """
        Verifica si el proyectil ha tocado al enemigo.
        """
        if self.proyectil.rect.colliderect(self.enemigo.rect) and not self.colisionada:
            self.colisionada = True
            self.enemigo.destruir()  # Eliminar el enemigo
            self.generar_estrella()  # Generar una estrella en la ubicación del enemigo
            return True
        return False

    def chequear_recogida_estrella(self):
        """
        Verifica si el personaje ha recogido la estrella.
        """
        if self.personaje.rect.colliderect(self.estrella_rect):
            self.contador_estrellas += 1  # Aumenta el contador de estrellas
            self.estrella_caida = False  # La estrella ha sido recogida
            return True
        return False

    def chequear_colision_personaje(self):
        """
        Verifica si un enemigo ha tocado al personaje, lo que reduce sus vidas.
        """
        if self.enemigo.rect.colliderect(self.personaje.rect):
            self.vidas -= 1  # El personaje pierde una vida
            if self.vidas <= 0:
                self.game_over()
            return True
        return False

    def generar_recompensa(self):
        """
        Genera una estrella en la posición donde el enemigo fue destruido.
        """
        if not self.estrella_caida:
            # Establecer la posición de la estrella
            self.estrella_pos = self.enemigo.rect.center
            # Ajuste para centrar la estrella
            self.estrella_rect.topleft = (
                self.estrella_pos[0] - 25, self.estrella_pos[1] - 25)
            self.estrella_caida = True

    def dibujar_animacion(self, screen):
        """
        Dibuja la animación de humo en la pantalla.
        :param screen: Superficie donde se dibujará la animación.
        """
        if self.colisionada:
            self.humo_rect.center = self.enemigo.rect.center
            screen.blit(self.animacion_humo_img, self.humo_rect)

    def dibujar_recompensa(self, screen):
        """
        Dibuja la estrella en la pantalla si ha caído.
        :param screen: Superficie donde se dibujará la estrella.
        """
        if self.estrella_caida:
            screen.blit(self.estrella_img, self.estrella_rect)

    def game_over(self):
        """
        Finaliza el juego cuando el personaje se queda sin vidas.
        """
        print("¡Juego terminado! Has perdido todas tus vidas.")
        pygame.quit()
        sys.exit()
