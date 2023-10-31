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

        if s == CLUBS:
            if v == ACE:
                self.name = "Ace of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(25, 0, self.width, self.height)
            elif v == TWO:
                self.name = "Two of Clubs"
                self.image = self.game.deck_spritesheet.get_sprite(80, 0, self.width, self.height)

        
        #COLLISION RECT
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y