import pygame

# размеры окна (размеры background.png)
WIDTH = 1125
HEIGHT = 633
FPS = 30
SCORE_LIMIT = 100

# Количество птиц... до автоматического завершения игры
ENEMIES_COUNT = 20

# menu settings
button_x = 200
button_y = 50
image_width = 300
image_height = 80


screen = pygame.display.set_mode(size=[WIDTH, HEIGHT])
pygame.display.set_caption('Catch birds!')
background = pygame.image.load('images/background.png')
background2 = pygame.image.load('images/background2.png')
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

cursor = pygame.image.load('images/cursor.png')
pygame.mouse.set_visible(False)
