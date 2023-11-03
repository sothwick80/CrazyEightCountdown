import pygame
from config import *
import math
import random

#for spritesheet with white bg
class BSpritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(BLACK)
        return sprite

class PlayingCard(pygame.sprite.Sprite):
    def __init__(self, game, x, y, s, v, h):
        self.game = game
        self._layer = CARD_LAYER

        #DISPLAY GROUPS
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        #SPRITE SIZE
        self.x = x# * 55
        self.y = y# * 67
        self.width = 55   
        self.height = 67

        #CARD VALUES
        self.suit = s
        self.facevalue = v
        self.place = h

        if h == 50:
            self.name = "Back of Card"
            self.image = self.game.deck_spritesheet.get_sprite(685, 268, self.width, self.height)
            
        if s == CLUBS:
            if v == ACE:
                self.name = "Ace of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(25, 0, self.width, self.height)
            elif v == TWO:
                self.name = "Two of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(80, 0, self.width, self.height)
            elif v == THREE:
                self.name = "Three of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(135, 0, self.width, self.height)
            elif v == FOUR:
                self.name = "Four of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(190, 0, self.width, self.height)
            elif v == FIVE:
                self.name = "Five of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(245, 0, self.width, self.height)
            elif v == SIX:
                self.name = "Six of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(300, 0, self.width, self.height)
            elif v == SEVEN:
                self.name = "Seven of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(355, 0, self.width, self.height)
            elif v == EIGHT:
                self.name = "Eight of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(410, 0, self.width, self.height)
            elif v == NINE:
                self.name = "Nine of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(465, 0, self.width, self.height)
            elif v == TEN:
                self.name = "Ten of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(520, 0, self.width, self.height)
            elif v == JACK:
                self.name = "Jack of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(575, 0, self.width, self.height)
            elif v == QUEEN:
                self.name = "Queen of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(630, 0, self.width, self.height)
            elif v == KING:
                self.name = "King of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(685, 0, self.width, self.height)
        elif s == SPADES:
            if v == ACE:
                self.name = "Ace of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(25, 67, self.width, self.height)
            elif v == TWO:
                self.name = "Two of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(80, 67, self.width, self.height)
            elif v == THREE:
                self.name = "Three of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(135, 67, self.width, self.height)
            elif v == FOUR:
                self.name = "Four of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(190, 67, self.width, self.height)
            elif v == FIVE:
                self.name = "Five of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(245, 67, self.width, self.height)
            elif v == SIX:
                self.name = "Six of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(300, 67, self.width, self.height)
            elif v == SEVEN:
                self.name = "Seven of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(355, 67, self.width, self.height)
            elif v == EIGHT:
                self.name = "Eight of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(410, 67, self.width, self.height)
            elif v == NINE:
                self.name = "Nine of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(465, 67, self.width, self.height)
            elif v == TEN:
                self.name = "Ten of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(520, 67, self.width, self.height)
            elif v == JACK:
                self.name = "Jack of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(575, 67, self.width, self.height)
            elif v == QUEEN:
                self.name = "Queen of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(630, 67, self.width, self.height)
            elif v == KING:
                self.name = "King of Spades"
                self.image = self.game.deck_spritesheet.get_sprite(685, 67, self.width, self.height)
        elif s == HEARTS:
            if v == ACE:
                self.name = "Ace of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(25, 134, self.width, self.height)
            elif v == TWO:
                self.name = "Two of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(80, 134, self.width, self.height)
            elif v == THREE:
                self.name = "Three of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(135, 134, self.width, self.height)
            elif v == FOUR:
                self.name = "Four of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(190, 134, self.width, self.height)
            elif v == FIVE:
                self.name = "Five of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(245, 134, self.width, self.height)
            elif v == SIX:
                self.name = "Six of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(300, 134, self.width, self.height)
            elif v == SEVEN:
                self.name = "Seven of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(355, 134, self.width, self.height)
            elif v == EIGHT:
                self.name = "Eight of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(410, 134, self.width, self.height)
            elif v == NINE:
                self.name = "Nine of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(465, 134, self.width, self.height)
            elif v == TEN:
                self.name = "Ten of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(520, 134, self.width, self.height)
            elif v == JACK:
                self.name = "Jack of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(575, 134, self.width, self.height)
            elif v == QUEEN:
                self.name = "Queen of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(630, 134, self.width, self.height)
            elif v == KING:
                self.name = "King of Hearts"
                self.image = self.game.deck_spritesheet.get_sprite(685, 134, self.width, self.height)
        elif s == DIAMONDS:
            if v == ACE:
                self.name = "Ace of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(25, 201, self.width, self.height)
            elif v == TWO:
                self.name = "Two of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(80, 201, self.width, self.height)
            elif v == THREE:
                self.name = "Three of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(135, 201, self.width, self.height)
            elif v == FOUR:
                self.name = "Four of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(190, 201, self.width, self.height)
            elif v == FIVE:
                self.name = "Five of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(245, 201, self.width, self.height)
            elif v == SIX:
                self.name = "Six of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(300, 201, self.width, self.height)
            elif v == SEVEN:
                self.name = "Seven of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(355, 201, self.width, self.height)
            elif v == EIGHT:
                self.name = "Eight of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(410, 201, self.width, self.height)
            elif v == NINE:
                self.name = "Nine of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(465, 201, self.width, self.height)
            elif v == TEN:
                self.name = "Ten of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(520, 201, self.width, self.height)
            elif v == JACK:
                self.name = "Jack of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(575, 201, self.width, self.height)
            elif v == QUEEN:
                self.name = "Queen of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(630, 201, self.width, self.height)
            elif v == KING:
                self.name = "King of Diamonds"
                self.image = self.game.deck_spritesheet.get_sprite(685, 201, self.width, self.height)
        #COLLISION RECT
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y