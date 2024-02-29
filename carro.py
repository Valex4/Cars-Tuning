import pygame

class Carro:
    def __init__(self, imagen, x, y, velocidad):
        self.imagen = imagen
        self.rect = imagen.get_rect(topleft=(x, y))
        self.velocidad = velocidad
        self.color = None  # Atributo para el color
        self.en_taller = False  # Seguimiento del estado en taller

    def mover(self, direccion):
        if not self.en_taller:
            self.rect.x += self.velocidad * direccion

    def cambiar_color(self, nuevo_color):
        self.imagen = pygame.image.load(os.path.join('assets', f'car-{nuevo_color}.png'))
        self.color = nuevo_color
