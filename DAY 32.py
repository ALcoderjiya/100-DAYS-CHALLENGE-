#DAY  32 DICE Game
import random
import time
import pygame
'''
name1 = input("Enter name of Player 1 :")
name2 = input("Enter name of Player 2 :")

val1 = random.randint(1,6)
val2  = random.randint(1,6)
time.sleep(2)
print("Player 1 got ",val1)
time.sleep(2)
print("Player 2 got ",val2)
time.sleep(2)
if val1 > val2:
    print(name1, " Wins !!!")
elif val1 < val2:
    print(name2," Wins !!!")
else:
    print("It's a Tie ")
'''
p = ["","","","","",""]
p[0] = pygame.image.load("1.jpg")
p[1] = pygame.image.load("2.jpg")
p[2] = pygame.image.load("3.jpg")
p[3] = pygame.image.load("4.jpg")
p[4] = pygame.image.load("5.jpg")
p[5] = pygame.image.load("6.jpg")

name1 = input("Enter Player 1's Name :")
name2 = input("Enter Player 2's Name :")
val1  = random.randint(1,6)
val2  = random.randint(1,6)
if val1 > val2:
    text3 = name1 + " Wins !!!"
elif val2 > val1:
    text3 = name2 + " WINS !!!"
else:
    text3 = "It's A DRAW"

pygame.init()
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
font = pygame.font.Font('freesansbold.ttf',32)

text1 = font.render(name1, True, green)
text2 = font.render(name2, True, green)
text3 = font.render(text3, True, green)

textRect1 = text1.get_rect()
textRect2 = text2.get_rect()
textRect3 = text3.get_rect()

textRect1.center = (150, 250)
textRect2.center = (350,250)
textRect3.center = (300,100)
win = pygame.display.set_mode((600,600))
while True:
    win.fill("black")
    win.blit(text1, textRect1)
    win.blit(text2, textRect2)
    win.blit(text3, textRect3)
    win.blit(p[val1 - 1], (100,300))
    win.blit(p[val2 - 1], (300,300))
    time.sleep(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    pygame.display.update()