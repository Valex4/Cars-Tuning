import pygame
import sys
import random
import threading
import time
import queue

# Inicializa Pygame
pygame.init()

# Configuración de la ventana
screen_width = 800
screen_height = 600

semaforo_width = 40
semaforo_height = 50

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("highway")

# Carga de imágenes
background_image = pygame.image.load('fondo.jpg')  # Imagen de la carretera
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
intersection_image = pygame.image.load('semaforo.png')  # Imagen de la intersección
intersection_image = pygame.transform.scale(intersection_image, (semaforo_width, semaforo_height))
car_image = pygame.image.load('Car.png')  # Imagen del vehículo (rectángulo)
semaphore_colors = [(0, 255, 0), (255, 255, 0), (255, 0, 0)]  # Colores de los semáforos

# Constantes
intersection_positions = [(200, 200), (400, 200), (600, 200)]  # Posiciones de las intersecciones
car_speed = 2  # Velocidad de los vehículos
num_cars = 20  # Número de vehículos
intersection_locks = [threading.Lock() for _ in range(len(intersection_positions))]  # Semáforos para cada intersección
semaphore_states = [0 for _ in range(len(intersection_positions))]  # Estado inicial de los semáforos
cars_stopped_count = [0 for _ in range(len(intersection_positions))]  # Contador de vehículos detenidos por semáforo

# Cola para notificaciones
notification_queue = queue.Queue()

# Clase para representar un vehículo
class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stopped = False

    def move(self):
        if not self.stopped:
            self.x += car_speed

# Función para mover los vehículos
def move_cars(cars, barrier):
    while True:
        barrier.wait()  # Esperar en la barrera antes de iniciar
        for car in cars:
            semaphore_index = min(car.x // 200, len(intersection_positions) - 1)  # Asegurar que el índice esté dentro del rango
            if semaphore_states[semaphore_index] != 0:  # Si el semáforo está en rojo
                car.stopped = True
                cars_stopped_count[semaphore_index] += 1  # Incrementar el contador de vehículos detenidos
            else:
                car.stopped = False
                car.move()
                if cars_stopped_count[semaphore_index] > 0:
                    cars_stopped_count[semaphore_index] -= 1  # Reducir el contador si el semáforo está en verde
        time.sleep(0.01)  # Retardo pequeño para controlar la velocidad

# Función para generar eventos aleatorios
def generate_events(event_barrier):
    while True:
        for i, count in enumerate(cars_stopped_count):
            if count > 10:  # Si hay más de 10 carros detenidos en un semáforo
                notification_queue.put(("¡Atención! Hay demasiado tráfico en el semáforo {}!".format(i + 1), time.time()))
        event_barrier.wait()  # Esperar en la barrera antes de generar eventos
        time.sleep(10)  # Generar eventos cada 10 segundos

# Función para dibujar las notificaciones
def draw_notifications():
    font = pygame.font.SysFont(None, 24)
    current_time = time.time()
    while not notification_queue.empty():
        notification, timestamp = notification_queue.get()
        if current_time - timestamp < 5:  # Mostrar la notificación solo durante 5 segundos
            text = font.render(notification, True, (255, 255, 255))
            window.blit(text, (10, 10))
        else:
            continue

# Función para dibujar los vehículos
def draw_cars(cars):
    for car in cars:
        resized_car_image = pygame.transform.scale(car_image, (50, 50))
        window.blit(resized_car_image, (car.x, car.y))

# Función para dibujar los semáforos
def draw_semaphores():
    for i, (x, y) in enumerate(intersection_positions):
        pygame.draw.circle(window, semaphore_colors[semaphore_states[i]], (x + 25, y + 25), 10)

# Función principal del juego
def main():
    cars = []
    car_barrier = threading.Barrier(2)  # Barrera para hilos de vehículos
    event_barrier = threading.Barrier(3)  # Barrera para generación de eventos

    # Crear hilos cooperativos
    for _ in range(2):
        car_thread = threading.Thread(target=move_cars, args=(cars, car_barrier))
        car_thread.daemon = True
        car_thread.start()

    for _ in range(10):
        car_barrier.wait()  # Esperar a que todos los hilos de vehículos estén listos

    event_thread = threading.Thread(target=generate_events, args=(event_barrier,))
    event_thread.daemon = True
    event_thread.start()

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for i, (x, y) in enumerate(intersection_positions):
                    if (x + 25 - 10) <= event.pos[0] <= (x + 25 + 10) and (y + 25 - 10) <= event.pos[1] <= (y + 25 + 10):
                        semaphore_states[i] = (semaphore_states[i] + 1) % 3  # Cambiar el estado del semáforo

        window.blit(background_image, (0, 0))

        for lock, (x, y) in zip(intersection_locks, intersection_positions):
            pygame.draw.rect(window, (255, 255, 255), pygame.Rect(x, y, 50, 50))  # Dibujar intersección
            lock.acquire()  # Bloquear el acceso a la intersección
            window.blit(intersection_image, (x, y))
            lock.release()  # Liberar el acceso a la intersección

        draw_semaphores()

        if random.randint(0, 100) < 5:  # Probabilidad de 5% de agregar un nuevo vehículo
            cars.append(Car(0, random.randint(0, screen_height - 20)))

        draw_cars(cars)

        draw_notifications()

        pygame.display.update()
        clock.tick(60)  # Limita el juego a 60 FPS

if __name__ == "__main__":
    main()
