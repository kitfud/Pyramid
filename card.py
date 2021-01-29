import pygame

class Card(pygame.sprite.Sprite):
  def __init__(self,rank,suit):
    super().__init__()
    self.rank = rank
    self.suit = suit 
    self.faceup = False 
    self.images = {True:pygame.image.load("images/cards/{} {}.png".format(suit,rank)),False:pygame.image.load("images/cards/Back Blue 1.png")}
    self.image = self.images[self.faceup]
    self.rect = self.image.get_rect()
  
  def flip(self):
    self.faceup= not self.faceup
    self.image = self.images[self.faceup]