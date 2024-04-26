import pygame
from button import ImageButton
from settings import *

pygame.init()

play_button = ImageButton(WIDTH/2-button_x,
                          100 + button_y,
                          image_width, image_height,
                          'PLAY',
                          'images/button06.png',
                          'images/button04.png',
                          'sounds/menu_sound.wav')

Levels_button = ImageButton(WIDTH/2-button_x,
                            100 + 3*button_y,
                            image_width, image_height,
                            'LEVELS',
                            'images/button06.png',
                            'images/button04.png',
                            'sounds/menu_sound.wav')
    
exit_button = ImageButton(WIDTH/2-button_x,
                          100 + 5*button_y,
                          image_width, image_height,
                          'EXIT',
                          'images/button06.png',
                          'images/button04.png',
                          'sounds/menu_sound.wav',
                          quit)

level1_button = ImageButton(WIDTH/2-button_x,
                            100 + button_y,
                            image_width, image_height,
                            'Level 1',
                            'images/button06.png',
                            'images/button04.png',
                            'sounds/menu_sound.wav')

level2_button = ImageButton(WIDTH/2-button_x,
                            100 + 3*button_y,
                            image_width, image_height,
                            'Level 2',
                            'images/button06.png',
                            'images/button04.png',
                            'sounds/menu_sound.wav')
back_level_button = ImageButton(WIDTH/2-button_x,
                                100 + 5*button_y,
                                image_width, image_height,
                                'BACK',
                                'images/button06.png',
                                'images/button04.png',
                                'sounds/menu_sound.wav')
back_result_button = ImageButton(WIDTH/2-button_x, 100 + 6*button_y,
                                 image_width, image_height,
                                 'BACK',
                                 'images/button06.png',
                                 'images/button04.png',
                                 'sounds/menu_sound.wav')
record_button = ImageButton(WIDTH/2-button_x, 100 + 4*button_y,
                            image_width, image_height,
                            'records',
                            'images/button06.png',
                            'images/button04.png',
                            'sounds/menu_sound.wav')
back_score_button = ImageButton(WIDTH/2-button_x, 350 + button_y,
                                image_width, image_height,
                                'MENU',
                                'images/button06.png',
                                'images/button04.png',
                                'sounds/menu_sound.wav')
