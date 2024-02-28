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

window = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Menú Inicial")

# Carga la imagen del menú desde la carpeta "assets"
menu_image = pygame.image.load(os.path.join('assets', 'Menu.jpg'))
button_start = pygame.image.load(os.path.join('assets', 'Play.png'))
button_exit = pygame.image.load(os.path.join('assets', 'Exit.png'))

# Ajusta el tamaño de la imagen al tamaño de la ventana
menu_image = pygame.transform.scale(menu_image, (screen_width, screen_height))
button_start = pygame.transform.scale(button_start, (button_width, button_height))
button_exit = pygame.transform.scale(button_exit, (button_width_exit, button_height_exit))

# Carga el GIF del nombre del juego desde la carpeta "assets"
name_game = pygame.image.load(os.path.join('assets', 'NombreJuego.png'))

# Ajusta el tamaño del GIF del nombre del juego
name_game = pygame.transform.scale(name_game, (name_width, name_height))

# Posiciones de los botones
button_start_x = 180
button_start_y = 350
button_exit_x = 400
button_exit_y = 350

name_x = 50  # Ajusta la posición horizontal del nombre del juego
name_y = 100   # Ajusta la posición vertical del nombre del juego

# Loop principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verifica si el clic del mouse está dentro del área del botón de inicio
            if button_start_x <= event.pos[0] <= button_start_x + button_width and \
                    button_start_y <= event.pos[1] <= button_start_y + button_height:
                print("¡Hola! Aquí iniciará el juego")
            # Verifica si el clic del mouse está dentro del área del botón de salida
            elif button_exit_x <= event.pos[0] <= button_exit_x + button_width_exit and \
                    button_exit_y <= event.pos[1] <= button_exit_y + button_height_exit:
                pygame.quit()
                sys.exit()

    # Muestra la imagen del menú en la ventana
    window.blit(menu_image, (0, 0))
    window.blit(button_start, (button_start_x, button_start_y))
    window.blit(button_exit, (button_exit_x, button_exit_y))
    window.blit(name_game, (name_x, name_y))

    pygame.display.update()

# Cierra Pygame
pygame.quit()
