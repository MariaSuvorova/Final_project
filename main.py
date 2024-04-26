import pygame
from menu import main_menu

pygame.init()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()
        main_menu()
pygame.quit()
quit()