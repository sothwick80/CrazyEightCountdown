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

        self.turn = 0 #1 - Player 1, 2 - Player 2

        #wilds tracker
        self.player_one_wild = 0
        self.player_two_wild = 0

        self.oncursor = False
        self.cursor_card = pygame.sprite.Sprite

        #sprite sheets
        self.deck_spritesheet = BSpritesheet('img/deck.jpg')

    def create_deck(self):
        #first index is back of playing card
        self.pu_deck.append(PlayingCard(self, 400, 400, 0, 0, 50))

        suits = HEARTS
        value = ACE
        while suits < 5:
            while value < 14:
                self.pu_deck.append(PlayingCard(self, -50, -50, suits, value, DECK))
                value += 1
            suits += 1
            value = ACE
        
        #LAST 2 ARE PLAYER STAGING

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
        temp = 0
        while temp < 8:
            self.player_one[temp].x = 100
            self.player_one[temp].y = 30 + (temp * 67)
            self.player_one[temp].rect = self.player_one[temp].image.get_rect()
            self.player_one[temp].rect.x = self.player_one[temp].x
            self.player_one[temp].rect.y = self.player_one[temp].y
            temp += 1

        temp = 0
        while temp < 8:
            self.player_two[temp].x = 600
            self.player_two[temp].y = 30 + (temp * 67)
            self.player_two[temp].rect = self.player_two[temp].image.get_rect()
            self.player_two[temp].rect.x = self.player_two[temp].x
            self.player_two[temp].rect.y = self.player_two[temp].y
            temp += 1

        self.turn = 1 #player 1s turn
        print ("It's Player 1s Turn !")

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
    ### MOUSE BUTTON DOWN ###
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.oncursor: #and collide with player 1 deck
                    if self.turn == 1:
                        print("Placing Player 1s Card on deck")
                        self.drop_deck.append(self.cursor_card)
                        self.oncursor = False
                        pygame.mouse.set_visible(True)
                        self.turn = 2
                    elif self.turn == 2:
                        print("Placing Player 2s Card on deck")
                        self.drop_deck.append(self.cursor_card)
                        self.oncursor = False
                        pygame.mouse.set_visible(True)
                        self.turn = 1
                else: #NOTHING ON CURSER
                    i=0
                    while i < self.pu_deck.__len__():
                        #if face down card is clicked
                        if self.pu_deck[i].rect.collidepoint(mouse_pos) and not self.oncursor:
                            print ("Picking Up Card from Deck")
                            self.oncursor = True
                            pygame.mouse.set_visible(False) 
                            self.cursor_card = self.pu_deck[i+1]        
                        i += 1
                    if self.turn == 1:
                        i=0
                        while i < self.player_one.__len__():
                            #if face down card is clicked
                            if self.player_one[i].rect.collidepoint(mouse_pos):
                                print ("Picking Up Card From Player 1s Deck")
                                self.oncursor = True
                                pygame.mouse.set_visible(False) 
                                self.cursor_card = self.player_one[i]        
                            i += 1
                    elif self.turn == 2:      
                        i=0
                        while i < self.player_two.__len__():
                            #if face down card is clicked
                            if self.player_two[i].rect.collidepoint(mouse_pos):
                                print ("Picking Up Card From Player 2s Deck")
                                self.oncursor = True
                                pygame.mouse.set_visible(False) 
                                self.cursor_card = self.player_two[i]        
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

g.new()
while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()