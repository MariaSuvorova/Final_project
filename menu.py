import pygame
import sys
from game import Game
from utils import print_text
from settings import *
from buttons import *
pygame.init()
from save import Save


def main_menu():
    running = True
    while running:
        screen.blit(background, (0, 0))
        print_text("MENU", WIDTH/2-(button_x/3), 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.USEREVENT and event.button == play_button:
                activate_lv2 = True
                game = Game(activate_lv2)
                result_score = game.level1_run()
                results(result_score)
            if event.type == pygame.USEREVENT and event.button == Levels_button:
                levels()

            for button in [play_button, Levels_button, exit_button]:
                button.handle_event(event)

        for button in [play_button, Levels_button, exit_button]:
            button.check_active(pygame.mouse.get_pos())
            button.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-3, y-3))

        clock.tick(FPS)
        pygame.display.flip()

def levels():
    running = True
    while running:
        screen.blit(background, (0, 0))
        print_text("LEVELS", WIDTH/2-(button_x/3), 100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.USEREVENT and event.button == level1_button:
                activate_lv2 = False
                game = Game(activate_lv2)
                result_score = game.level1_run()
                results(result_score)

            if event.type == pygame.USEREVENT and event.button == level2_button:
                activate_lv2 = False
                game = Game(activate_lv2)
                result_score = game.level2_run()
                results(result_score)

            if event.type == pygame.USEREVENT and event.button == back_level_button:
                main_menu()

            for button in [level1_button, level2_button, back_level_button]:
                button.handle_event(event)

        for button in [level1_button, level2_button, back_level_button]:
            button.check_active(pygame.mouse.get_pos())
            button.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-3, y-3))

        pygame.display.flip()
        clock.tick(FPS)

def results(score):

    input_box = pygame.Rect(WIDTH/2-button_x/2-50, 100 + 2*button_y, button_x, button_y)
    color_inactive = pygame.Color((20, 150, 10))
    color_active = pygame.Color((255, 0, 155))
    color = color_inactive
    active = False
    text = '|'
    input_tick = 30
    save_data = Save()
    running = True
    while running:
        screen.blit(background, (0, 0))
        print_text(f'Game over! Final score: {score}', WIDTH/2-(button_x/3), 100)
        print_text(f'Enter your name:', WIDTH/2-(button_x/3), 150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #  back to previous menu
            if event.type == pygame.USEREVENT and event.button == back_result_button:
                running = False

            if event.type == pygame.USEREVENT and event.button == record_button:
                score_table(save_data.print_table())
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False
            color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    text = text.replace('|', '')
                    input_tick = 30
                    if event.key == pygame.K_RETURN:
                        active = False
                        text = text if text else 'player'
                        save_data.save(text, score)
                        results_saved(text, score, save_data.print_table())
                        # text = ''
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        if len(text) < 10:
                            text += event.unicode

                    text += '|'

            for button in [back_result_button, record_button]:
                button.handle_event(event)
            
            save_data.close

        for button in [back_result_button, record_button]:
            button.check_active(pygame.mouse.get_pos())
            button.draw(screen)

        input_tick -= 1

        if input_tick == 0:
            text = text[:-1]
        if input_tick == -30:
            text = '|'
            input_tick = 30

        # Render the current text.
        font = pygame.font.Font('fonts/Caveat-Regular.ttf', 36)
        txt_surface = font.render(text, True, color)

        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-3, y-3))

        pygame.display.flip()
        clock.tick(30)

def results_saved(name, score, highscores):

    running = True
    while running:
        screen.blit(background, (0, 0))
        print_text(f'{name}!', WIDTH/2-50, 100)
        print_text(f'your score {score} saved', WIDTH/2-(button_x/3), 150)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #  back to previous menu
            if event.type == pygame.USEREVENT and event.button == back_result_button:
                running = False

            if event.type == pygame.USEREVENT and event.button == record_button:
                score_table(highscores)
        
            for button in [back_result_button, record_button]:
                button.handle_event(event)

        for button in [back_result_button, record_button]:
            button.check_active(pygame.mouse.get_pos())
            button.draw(screen)

        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-3, y-3))

        pygame.display.flip()
        clock.tick(30)

def score_table(highscores):
    running = True
    while running:
        screen.blit(background, (0, 0))
        print_text('Records:', WIDTH/2-50, 100)
        keys = list()
        values = list()
        for key, value in highscores:
            keys.append(key)
            values.append(value)

        n = len(keys) if len(keys) < 5 else 5

        for i in range(0, n):
            print_text(f'{keys[i]}', WIDTH/2-(button_x/3)-20, 150 + i*50)
            print_text(f'{values[i]}', WIDTH/2, 150 + i*50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()

            #  возврат в меню
            if event.type == pygame.USEREVENT and event.button == back_score_button:
                running = False
                main_menu()

            for button in [back_score_button]:
                button.handle_event(event)

        for button in [back_score_button]:
            button.check_active(pygame.mouse.get_pos())
            button.draw(screen)
        
        x, y = pygame.mouse.get_pos()
        screen.blit(cursor, (x-3, y-3))
            
        pygame.display.flip()
        clock.tick(30)
