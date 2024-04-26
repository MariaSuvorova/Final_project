import pygame
from settings import *


def print_text(message, x, y, font_color=(255, 0, 155), 
               font_type = 'fonts/Caveat-Regular.ttf', 
               font_size = 36):
    font = pygame.font.Font(font_type, font_size)
    text_block = font.render(message, True, font_color)
    text_rect = text_block.get_rect(center=(x, y))
    screen.blit(text_block, text_rect)
