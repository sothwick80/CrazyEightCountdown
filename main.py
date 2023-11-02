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
        self.pu_deck = []
        self.drop_deck = []
        self.player_one = []
        self.player_two = []

        #wilds tracker
        self.player_one_wild = 0
        self.player_two_wild = 0

        self.oncursor = False
        self.cursor_card = pygame.sprite.Sprite

        #sprite sheets
        self.deck_spritesheet = BSpritesheet('img/deck.jpg')

    def create_deck(self):
        suits = HEARTS
        value = ACE
        while suits < 5:
            while value < 14:
                self.pu_deck.append(PlayingCard(self, 10, 10, suits, value, DECK))
                value += 1
            suits += 1
            value = ACE

        print ("there are ",self.pu_deck.__len__(), "elements in the list")

    def deal_next(self, player):
        #if the wild is 0, player wins
        #if self.pu_deck.len__() < amount needed
        #grab self.drop_deck - last played cards, shuffle, add to self.pu_deck  
        if player == 1:
            self.player_one_wild -= 1
            dealt = 0
            while dealt < self.player_one_wild:
                self.player_one.append(self.pu_deck.pop())
                dealt += 1

    def new(self):
        self.playing = True

        # ALL SPRITES TO BE DRAWN MUST GO HERE
        self.all_sprites = pygame.sprite.LayeredUpdates()

        self.create_deck()
        random.shuffle(self.pu_deck)

        #deal cards
        dealt = 0
        while dealt < 8:
            self.player_one.append(self.pu_deck.pop())
            self.player_two.append(self.pu_deck.pop())
            dealt += 1
        
        self.player_one_wild = EIGHT
        self.player_two_wild = EIGHT

        #display hands

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                i = 0
                while i < self.pu_deck.__len__():
                    if self.pu_deck[i].rect.collidepoint(mouse_pos):
                        print ("Picking Up Card")
                        self.oncursor = True
                        pygame.mouse.set_visible(False) 
                        self.cursor_card = self.pu_deck[i]               
                        #self.menuboxes[CURSOR] = self.party[self.top_character].inventory[PRIMARY]
                        #self.inventory_flag[PRIMARY] = False
                    i += 1 

    def update(self):
        if self.oncursor:
            self.cursor_card.rect.center = pygame.mouse.get_pos()
            #self.menuboxes[CURSOR].rect.center = pygame.mouse.get_pos()
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