import pygame

class Taller:
    def __init__(self, x, y, ancho, alto, capacidad):
        self.rect = pygame.Rect(x, y, ancho, alto)
        self.cola = []
        self.capacidad = capacidad
        self.carro_actual = None  # Seguimiento del carro actual en taller

    def comprobar_entrada(self, carro):
        if carro.rect.colliderect(self.rect) and not self.esta_lleno():
            self.cola.append(carro)
            carro.en_taller = True

    def esta_lleno(self):
        return len(self.cola) >= self.capacidad

    def procesar_cola(self):
        if self.carro_actual is None and self.cola:
            self.carro_actual = self.cola.pop(0)
            self.carro_actual.cambiar_color(random.choice(COLORES))  # Color aleatorio

        if self.carro_actual:
            # Simular tiempo de procesamiento (reemplazar con la lógica deseada)
            tiempo_procesamiento = 2  # Ajustar según se necesite
            pygame.time.wait(tiempo_procesamiento * 1000)  # Esperar en milisegundos
            self.carro_actual.en_taller = False
            self.carro_actual = None
