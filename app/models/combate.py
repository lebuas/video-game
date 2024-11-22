
class Combate:
    def __init__(self, personaje, enemigos, proyectiles, proyectiles_enemigos, trampas):
        self.personaje = personaje
        self.enemigos = enemigos
        self.proyectiles = proyectiles
        self.proyectiles_enemigos = proyectiles_enemigos
        self.trampas = trampas  # Lista de trampas
        self.explosiones = []  # Lista para almacenar explosiones activas

    def chequear_colisiones(self):
        resultados_colision = []
        #
        # # Verificar colisión con trampas
        # resultado = self.colision_trampa_personaje()
        # if resultado:
        #     resultados_colision.append(resultado)

        # Verificar colisión con bala del enemigo
        resultado = self.colision_bala_personaje()
        if resultado:
            resultados_colision.append(resultado)

        # Verificar colisión con bala del personaje
        resultado = self.colision_bala_enemigo()
        if resultado:
            resultados_colision.append(resultado)

        # Verificar colisión entre balas
        resultado = self.colision_bala_bala()
        if resultado:
            resultados_colision.append(resultado)

        return resultados_colision

    # def colision_trampa_personaje(self):
    #     """Revisa si la trampa colisiona con el personaje o con el suelo."""
    #     resultados_colision = []
    #
    #     for trampa in self.trampas[:]:
    #         # Verificar si la trampa ha llegado al suelo
    #         if trampa.rect.bottom >= self.personaje.suelo_y:  # Suelo del escenario
    #             # Verificar si el personaje está en el rango de la trampa
    #             distancia = abs(self.personaje.rect.centerx -
    #                             trampa.rect.centerx)
    #             if distancia <= trampa.rango_daño:  # Si está dentro del rango de la trampa
    #                 if trampa.nivel == 1:
    #                     self.personaje.perder_vida()  # Quita 1 vida
    #                 elif trampa.nivel == 2:
    #                     self.personaje.vidas -= 2  # Quita 2 vidas
    #                 elif trampa.nivel == 3:
    #                     self.personaje.vidas = 0  # Muerte instantánea
    #
    #                 # Eliminar la trampa tras el impacto
    #                 self.trampas.remove(trampa)
    #
    #                 resultados_colision.append({
    #                     "tipo": "impacto trampa",
    #                     "coordenadas": (self.personaje.rect.centerx, self.personaje.rect.centery),
    #                     "nivel_trampa": trampa.nivel
    #                 })
    #     return resultados_colision

    def colision_bala_personaje(self):
        """Revisa si una bala enemiga impacta al personaje y reduce su vida."""
        for proyectil_enemigo in self.proyectiles_enemigos[:]:
            if self.personaje.rect.colliderect(proyectil_enemigo.rect):
                self.proyectiles_enemigos.remove(proyectil_enemigo)
                return {
                    "tipo": "impacto personaje",
                    "coordenadas": (self.personaje.rect.centerx, self.personaje.rect.centery)
                }
        return None

    def colision_bala_enemigo(self):
        """Revisa si una bala del personaje impacta a un enemigo."""
        for proyectil in self.proyectiles[:]:
            for enemigo in self.enemigos[:]:
                if enemigo.rect.colliderect(proyectil.rect):
                    self.enemigos.remove(enemigo)
                    self.proyectiles.remove(proyectil)
                    return {
                        "tipo": "impacto enemigo",
                        "coordenadas": (enemigo.rect.centerx, enemigo.rect.centery)
                    }
        return None

    def colision_bala_bala(self):
        """Revisa si una bala del personaje colisiona con una bala enemiga."""
        for proyectil_personaje in self.proyectiles[:]:
            for proyectil_enemigo in self.proyectiles_enemigos[:]:
                if proyectil_personaje.rect.colliderect(proyectil_enemigo.rect):
                    punto_colision = proyectil_personaje.rect.clip(
                        proyectil_enemigo.rect).center
                    self.proyectiles.remove(proyectil_personaje)
                    self.proyectiles_enemigos.remove(proyectil_enemigo)
                    return {
                        "tipo": "impacto entre balas",
                        "coordenadas": punto_colision
                    }
        return None
