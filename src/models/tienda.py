import pygame


class Tienda:
    def __init__(self):
        self.naves_disponibles = ["nave_nivel_1.png",
                                  "nave_nivel_2.png", "nave_nivel_3.png"]
        self.precio_nave = 50  # Precio por cada nave

    def comprar_nave(self, recompensas, personaje):
        if recompensas >= self.precio_nave:
            # Cambiar la nave del personaje
            personaje.imagen = pygame.image.load(
                self.naves_disponibles[1])  # Ejemplo, nave nivel 2
            recompensas -= self.precio_nave  # Descontar el precio
        return recompensas
