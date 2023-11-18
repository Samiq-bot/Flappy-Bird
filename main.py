import sys
import random
import pygame
from pygame.locals import *


FPS = 32
SCREENWIDTH = 290
SCREENHEIGHT = 500
SCREEN = pygame.display.set_mode(SCREENWIDTH, SCREENHEIGHT)
GROUNDY = SCREENHEIGHT * 0.8
GAME_SPRITES = {}
GAME_SOUNDS = {}
PLAYER = '/Resources/images/bird.png'
BACKGROUND = '/Resources/images/background.png'
PIPE = '/Resources/images/pipes.png'


# this is where the gamne will start

if __name__ == '__main__':
    pygame.init()
# it initializes pygame all pygame modules

FPS_CLOCK = pygame.time.Clock()
pygame.display.set_caption('Flappy Bird by Samiq')
GAME_SPRITES['Number'] = (
    pygame.image.load('/Resources/images/0.png').convert_alpha(),
    pygame.image.load('/Resources/images/1.png').convert_alpha(),
    pygame.image.load('/Resources/images/2.png').convert_alpha(),
    pygame.image.load('/Resources/images/3.png').convert_alpha(),
    pygame.image.load('/Resources/images/4.png').convert_alpha(),
    pygame.image.load('/Resources/images/5.png').convert_alpha(),
    pygame.image.load('/Resources/images/6.png').convert_alpha(),
    pygame.image.load('/Resources/images/7.png').convert_alpha(),
    pygame.image.load('/Resources/images/8.png').convert_alpha(),
    pygame.image.load('/Resources/images/9.png').convert_alpha(),
    )
GAME_SPRITES['message'] = pygame.image.load('/Resources/images/message.png').convert_alpha()
GAME_SPRITES['base'] = pygame.image.load('/Resources/images/base.png').convert_alpha()
GAME_SPRITES['pipes'] = (
    pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha()), 180,
    pygame.image.load(PIPE).convert_alpha(),
    )










