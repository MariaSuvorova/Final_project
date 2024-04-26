import pygame
from utils import print_text

class ImageButton:

    def __init__(self, x, y, width, height, text, image_path, active_image_path=None, sound_path=None, action = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.action = action

        # подгоняем размер картинки под заданные размеры кнопки
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))

        self.active_image = self.image
        if active_image_path:
            self.active_image = pygame.image.load(active_image_path)
            self.active_image = pygame.transform.scale(self.active_image, (width, height))

        self.rect = self.image.get_rect(topleft=(x, y))

        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)

        self.is_active = False

    def draw(self, screen):
        current_image = self.active_image if self.is_active else self.image
        screen.blit(current_image, self.rect.topleft)

        print_text(self.text, self.rect.centerx, self.rect.centery)

    def check_active(self, mouse_pos):
        self.is_active = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1 and self.is_active:
            if self.sound:
                self.sound.play()
            if self.action is not None:
                if self.action == quit:
                    pygame.quit()
                    quit()
                self.action()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))
