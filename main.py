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

selected_card = pygame.sprite.GroupSingle()

def check_sprite_clicked(x,y):
  card_clicked = None
  for card in board:
    if card.rect.collidepoint(x,y):
      card_clicked = card
    if card_clicked is not None:
      hit_list = pygame.sprite.spritecollide(card_clicked,board,False)
      for card in hit_list:
        if card.rect.y > card_clicked.rect.y:
          return
      selected_card.add(card_clicked)

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
      if event.type == MOUSEBUTTONDOWN:
        if event.button ==1:
          x,y = event.pos
          check_sprite_clicked(x,y)
      screen.fill(bg_color)
      board.draw(screen)
      if len(selected_card) == 1:
        pygame.draw.rect(screen,(204,173,0),selected_card.sprite.rect,3)
      pygame.display.flip()

if __name__ =="__main__":
  main()
