import sys
import pygame
from random import randint
from game_objects.player import Player
from game_objects.bird import Bird
from game_objects.plant import Plant
from utils import print_text
from settings import *
pygame.init()


class Game:
    def __init__(self, activate_lv2):
        self.score = 0
        self.activate_lv2 = activate_lv2

    def level1_run(self):
        # Частота генерации птиц (мс)
        appearance_frequency = 2000
        appearance_speeding = 200

        BIRDADD = pygame.USEREVENT + 1
        pygame.time.set_timer(BIRDADD, appearance_frequency)

        bird_list = pygame.sprite.Group()

        player = Player('images/cruncher')
        player.update(pygame.mouse.get_pos())

        running = True
        while running:
            screen.blit(background, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                elif event.type == BIRDADD:
                    new_bird = Bird('images/green_bird/right',
                                    randint(1, 10), 0,
                                    randint(0, HEIGHT - 40))
                    bird_list.add(new_bird)
                    new_bird = Bird('images/green_bird/left',
                                    -randint(1, 10), WIDTH - 44,
                                    randint(0, HEIGHT - 40))
                    bird_list.add(new_bird)
                    new_bird = Bird('images/yellow_bird/right',
                                    randint(1, 10), 0,
                                    randint(0, HEIGHT - 40))
                    bird_list.add(new_bird)
                    new_bird = Bird('images/yellow_bird/left',
                                    -randint(1, 10), WIDTH - 44,
                                    randint(0, HEIGHT - 40))
                    bird_list.add(new_bird)

                    if len(bird_list) < 5:
                        appearance_frequency -= appearance_speeding*2

                    if appearance_frequency < 200:
                        appearance_frequency = 200

                    pygame.time.set_timer(BIRDADD, 0)
                    pygame.time.set_timer(BIRDADD, appearance_frequency)

            player.update(pygame.mouse.get_pos())

            bird_catched = pygame.sprite.spritecollide(sprite=player,
                                                       group=bird_list,
                                                       dokill=True)
            for bird in bird_catched:
                self.score += 10

            if self.score == SCORE_LIMIT:
                if self.activate_lv2:
                    running = False
                    return(self.level2_run())

            # Автоматическое закрытие игры при лимите ENEMIES_COUNT
            if len(bird_list) >= ENEMIES_COUNT:
                running = False
                return self.score
            # отрисовка птиц
            for bird in bird_list:
                bird.update()
                screen.blit(bird.surf, bird.rect)
            # отрисовка player
            screen.blit(player.surf, player.rect)

            # счет
            print_text(f"Score: {self.score}", WIDTH/2 - 50, 40)

            pygame.display.flip()
            clock.tick(FPS)

    def level2_run(self):
        screen.blit(background2, (0, 0))

        if self.activate_lv2:
            print_text(f"You reached score: {SCORE_LIMIT}", WIDTH/2 - 50, 60, font_size=55)
            print_text("Level 2 start . . .", WIDTH/2 - 50, 120, font_size=55)
            pygame.display.flip()
            pygame.time.wait(2000)

        # Частота генерации птиц... (мс)
        appearance_frequency = 1500
        appearance_speeding = 200

        BIRDADD = pygame.USEREVENT + 2
        pygame.time.set_timer(BIRDADD, appearance_frequency)

        PLANTDADD = pygame.USEREVENT + 3
        pygame.time.set_timer(PLANTDADD, appearance_frequency-500)

        bird_list = pygame.sprite.Group()
        speed_bird_list = pygame.sprite.Group()
        plant_list = pygame.sprite.Group()

        player = Player('images/cruncher')
        player.update(pygame.mouse.get_pos())

        if self.activate_lv2:
            self.score = SCORE_LIMIT

        running = True
        while running:
            screen.blit(background2, (0, 0))

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()

                elif event.type == PLANTDADD:
                    new_plant = Plant('images/plant/left', randint(1, WIDTH-44), HEIGHT-59)
                    plant_list.add(new_plant)
                    new_plant = Plant('images/plant/right', randint(1, WIDTH-44), HEIGHT-59)
                    plant_list.add(new_plant)

                elif event.type == BIRDADD:
                    new_bird = Bird('images/green_bird/right', randint(1, 10), 0,
                                    randint(0, HEIGHT-90))
                    bird_list.add(new_bird)

                    new_bird = Bird('images/green_bird/left', -randint(1, 10),
                                    WIDTH-44, randint(0, HEIGHT-90))
                    bird_list.add(new_bird)

                    new_bird = Bird('images/yellow_bird/right', randint(1, 10), 0,
                                    randint(0, HEIGHT-90))
                    bird_list.add(new_bird)

                    new_bird = Bird('images/yellow_bird/left', -randint(1, 10),
                                    WIDTH-44, randint(0, HEIGHT-90))
                    bird_list.add(new_bird)

                    if len(bird_list) < 5:
                        appearance_frequency -= appearance_speeding*2

                    if appearance_frequency < 300:
                        appearance_frequency = 300

                    if len(bird_list) + len(plant_list) > 8:
                        new_bird = Bird('images/red_bird/right', randint(15, 20), 0,
                                        randint(0, HEIGHT-90))
                        speed_bird_list.add(new_bird)

                    if len(bird_list) + len(plant_list) > 10:
                        new_bird = Bird('images/red_bird/left', -randint(15, 20),
                                        WIDTH-44, randint(0, HEIGHT-90))
                        speed_bird_list.add(new_bird)

                    pygame.time.set_timer(BIRDADD, 0)
                    pygame.time.set_timer(BIRDADD, appearance_frequency)

            player.update(pygame.mouse.get_pos())

            bird_catched = pygame.sprite.spritecollide(sprite=player,
                                                       group=bird_list,
                                                       dokill=True)

            speed_bird_catched = pygame.sprite.spritecollide(sprite=player,
                                                             group=speed_bird_list,
                                                             dokill=True)
            plant_catched = pygame.sprite.spritecollide(sprite=player,
                                                        group=plant_list,
                                                        dokill=True)

            for bird in bird_catched:
                self.score += 10

            for bird in speed_bird_catched:
                self.score += 20

            for plant in plant_catched:
                self.score += 5

            # Автоматическое закрытие игры при лимите ENEMIES_COUNT
            if len(bird_list) + len(speed_bird_list) + len(plant_list) >= ENEMIES_COUNT+10:
                running = False
                return self.score

            # отрисовка птиц...
            for bird in bird_list:
                bird.update()
                screen.blit(bird.surf, bird.rect)
            for bird in speed_bird_list:
                bird.update()
                screen.blit(bird.surf, bird.rect)
            for plant in plant_list:
                plant.update()
                screen.blit(plant.surf, plant.rect)

            # отрисовка player
            screen.blit(player.surf, player.rect)

            # счет
            print_text(f"Score: {self.score}", WIDTH/2 - 50, 40)

            pygame.display.flip()
            clock.tick(30)
