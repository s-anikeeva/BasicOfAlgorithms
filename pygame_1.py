import pygame
from pygame.locals import *
WIDTH = 800
HEIGHT = 650
FPS = 60
BLACK = (0, 0, 0)
RUNNING = True
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50, 50))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
    def update_right(self):
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0
    def update_left(self):
        self.rect.x -= 5
        if self.rect.right > WIDTH:
            self.rect.left = 0
    def update_down(self):
        self.rect.y += 5
        if self.rect.top > WIDTH:
            self.rect.top = 0
    def update_top(self):
        self.rect.y -= 5
        if self.rect.top > WIDTH:
            self.rect.top = 0

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Моя игра")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)


while RUNNING:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if pygame.key.get_pressed()[K_RIGHT]:
            player.update_right()
        if pygame.key.get_pressed()[K_LEFT]:
            player.update_left()
        if pygame.key.get_pressed()[K_DOWN]:
            player.update_down()
        if pygame.key.get_pressed()[K_UP]:
            player.update_top()
    all_sprites.update()
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
pygame.quit()
