import pygame, sys
from pygame.locals import *
from deck import *

deck = None
pygame.init()
board = pygame.sprite.Group()
size = (width,height) = (700,500)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
bg_color = (0,102,0)

def init():
  global deck
  deck = Deck()
  for i in range(7):
    for j in range(i+1):
      card = deck.deal()
      card.rect.midtop = (width//2-40*i + 80*j,30 + 30*i)
      card.flip()
      board.add(card)

def main():
  global screen 
  init()
  while True:
    clock.tick(60)
    for event in pygame.event.get():
      if event.type == QUIT:
        sys.exit()
      if event.type == KEYDOWN:
        if event.key == K_f:
          screen = pygame.display.set_mode(size,FULLSCREEN)
        elif event.key == K_ESCAPE:
          screen = pygame.display.set_mode(size)
      screen.fill(bg_color)
      board.draw(screen)
      pygame.display.flip()

if __name__ =="__main__":
  main()
