import pygame
import os
import sys

# Inicializa Pygame
pygame.init()

# Configura la ventana
screen_width = 800
screen_height = 600

name_width = 700
name_height = 200

button_width = 200
button_height = 100

button_width_exit = 190
button_height_exit = 100


taller_width = 300
taller_height = 200

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menú Inicial")

# Carga la imagen del menú desde la carpeta "assets"
menu_image = pygame.image.load(os.path.join('assets', 'Menu.jpg'))
button_start = pygame.image.load(os.path.join('assets', 'Play.png'))
button_exit = pygame.image.load(os.path.join('assets', 'Exit.png'))
car_pink = pygame.image.load(os.path.join('assets', 'car-pink.png'))
car_green = pygame.image.load(os.path.join('assets', 'car-green.png'))
car_red = pygame.image.load(os.path.join('assets', 'car-red.png'))
taller_image = pygame.image.load(os.path.join('assets', 'taller.png'))

# Ajusta el tamaño de la imagen al tamaño de la ventana
menu_image = pygame.transform.scale(menu_image, (screen_width, screen_height))
button_start = pygame.transform.scale(button_start, (button_width, button_height))
button_exit = pygame.transform.scale(button_exit, (button_width_exit, button_height_exit))

# Carga el GIF del nombre del juego desde la carpeta "assets"
name_game = pygame.image.load(os.path.join('assets', 'NombreJuego.png'))

# Ajusta el tamaño del GIF del nombre del juego
name_game = pygame.transform.scale(name_game, (name_width, name_height))

# Ajusta el tamaño de la imagen del taller
taller_image = pygame.transform.scale(taller_image, (taller_width, taller_height))

# Posiciones de los botones
button_start_x = 180
button_start_y = 350
button_exit_x = 400
button_exit_y = 350

name_x = 50  # Ajusta la posición horizontal del nombre del juego
name_y = 100   # Ajusta la posición vertical del nombre del juego

taller_x = (screen_width - taller_width) // 2
taller_y = (screen_height - taller_height) // 1


car_pink_x = 200  # Posición inicial del carro rosa
car_pink_y = 450
car_pink_speed = 1  # Velocidad del carro rosa

car_green_x = 200  # Posición inicial del carro verde
car_green_y = 350
car_green_speed = 2  # Velocidad del carro verde

car_red_x = 200  # Posición inicial del carro rojo
car_red_y = 250
car_red_speed = 3  # Velocidad del carro rojo

game_started = False  # Variable para controlar si el juego ha comenzado

# Loop principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not game_started:
                game_started = True
                button_start = pygame.Surface((0, 0))  # Hace que el botón de inicio desaparezca
                button_exit = pygame.Surface((0, 0))   # Hace que el botón de salida desaparezca
                print("¡El juego ha comenzado!")

    if game_started:
        car_pink_x += car_pink_speed  # Mueve el carro rosa automáticamente hacia la derecha
        car_green_x += car_green_speed  # Mueve el carro verde automáticamente hacia la derecha
        car_red_x += car_red_speed  # Mueve el carro rojo automáticamente hacia la derecha

        # Si alguno de los carros sale completamente de la pantalla, reinicia su posición
        if car_pink_x > screen_width:
            car_pink_x = -car_pink.get_width()
        if car_green_x > screen_width:
            car_green_x = -car_green.get_width()
        if car_red_x > screen_width:
            car_red_x = -car_red.get_width()

    # Muestra la imagen del menú en la ventana
    window.blit(menu_image, (0, 0))
    window.blit(button_start, (button_start_x, button_start_y))
    window.blit(button_exit, (button_exit_x, button_exit_y))
    window.blit(name_game, (name_x, name_y))
    window.blit(taller_image, (taller_x, taller_y))
    window.blit(car_pink, (car_pink_x, car_pink_y))
    window.blit(car_green, (car_green_x, car_green_y))
    window.blit(car_red, (car_red_x, car_red_y))

    pygame.display.update()

# Cierra Pygame
pygame.quit()
sys.exit()