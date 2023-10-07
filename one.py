import pygame
import time
pygame.init()
from random import randint

back = (200, 255, 255)

mw = pygame.display.set_mode((500,500))
mw.fill(back)
clock = pygame.time.Clock()

class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw,self.fill_color,self.rect)

    def redd(self, frame_color, thiskness):
        pygame.draw.rect(mw, frame_color,self.rect, thiskness)
    
    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Label(Area):
    def set_text(self, text, fsize =12, text_color=(0,0,0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text,True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x,self.rect.y+shift_y))
r = (255, 0,0)
g = (0, 255, 51)
y = (255, 255, 0)
d_b = (0,0,100)
b = (80,80,255)

cards = []
num_cards = 4
x = 70
for  i in range(num_cards):
    new_card = Label(x, 170,70,100, y) 
    new_card.redd(b,10)
    new_card.set_text('CLICK',26)
    cards.append(new_card)
    x = x + 100

wait = 0

while True:
    if wait == 0:
        wait = 20
        click = randint(1, num_cards)
        for i in range(num_cards):
            cards[i].color(y)
            if (i + 1) == click:
                cards[i].draw(10, 40)
            else:
                cards[i].fill()
    else:
        wait -= 1
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x, y = event.pos
            for i in range (num_cards):
                if cards[i].collidepoint(x, y):
                    if i + 1 == click:
                        cards[i].color(g)  
                    else:
                        cards[i].color(r)
                    cards[i].fill()


    pygame.display.update()
    clock.tick(40)
