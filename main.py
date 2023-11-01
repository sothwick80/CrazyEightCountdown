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

        #DECKS
        self.deck = []
        self.player_one = []
        self.player_two = []

        #sprite sheets
        self.deck_spritesheet = BSpritesheet('img/deck.jpg')

    def create_deck(self):
        suits = HEARTS
        value = ACE
        while suits < 5:
            while value < 14:
                self.deck.append(PlayingCard(self, 10, 10, suits, value, DECK))
                value += 1
            suits += 1

    def new(self):
        self.playing = True

        # ALL SPRITES TO BE DRAWN MUST GO HERE
        self.all_sprites = pygame.sprite.LayeredUpdates()

        self.create_deck()
        random.shuffle(self.deck)

        #deal cards


    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

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