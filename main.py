import pygame
import sys
from sprites import *
from config import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('trebuc.ttf', 32)
        self.running = True

    #sprite sheets
    self.deck_spritesheet = WSpritesheet('img/deck.jpg')



    def new(self):
        self.playing = True

        # ALL SPRITES TO BE DRAWN MUST GO HERE
        self.all_sprites = pygame.sprite.LayeredUpdates()


    def events(self):
        for event in pygame.event.get():
            pass

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main(self):
        #main game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def game_over(self):
        for sprite in self.all_sprites:
            sprite.kill()


g = Game()
#g.intro_screen()
g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()