#DAY 66 INPUT NAMES AND SHOW IMAGES
import pygame
import random
from pygame import mixer
name = input("Enter Your Name : ")
pygame.init()

clr = (0,0,0)
w = len(name)*100+100
win = pygame.display.set_mode((w,500))

#set the pygame window name
pygame.display.set_caption('My Name')
t = { }
t['a'] = pygame.image.load("A.png")
t['b'] = pygame.image.load("B.png")
t['c'] = pygame.image.load("C.png")
t['d'] = pygame.image.load("D.png")
t['e'] = pygame.image.load("E.png")
t['f'] = pygame.image.load("F.png")
t['g'] = pygame.image.load("G.png")
t['h'] = pygame.image.load("H.png")
t['i'] = pygame.image.load("I.png")
t['j'] = pygame.image.load("J.png")
t['k'] = pygame.image.load("K.png")
t['l'] = pygame.image.load("L.png")
t['m'] = pygame.image.load("M.png")
t['n'] = pygame.image.load("N.png")
t['o'] = pygame.image.load("O.png")
t['p'] = pygame.image.load("P.png")
t['q'] = pygame.image.load("Q.png")
t['r'] = pygame.image.load("R.png")
t['s'] = pygame.image.load("S.png")
t['t'] = pygame.image.load("T.png")
t['u'] = pygame.image.load("U.png")
t['v'] = pygame.image.load("V.png")
t['w'] = pygame.image.load("W.png")
t['x'] = pygame.image.load("X.png")
t['y'] = pygame.image.load("Y.png")
t['z'] = pygame.image.load("Z.png")
img = []
for ch in name.lower():
    img.append(t[ch])

mixer.init()
mixer.music.load("new.mp3")
mixer.music.set_volume(0.10)
mixer.music.play()
while True:


    win.fill(clr)
    x = 50
    for i in img:

        win.blit(i,(x,50))
        x += 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()