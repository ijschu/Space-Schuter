import pygame

space_tile = pygame.image.load("sprites\Backgrounds\darkPurple.png")

TILESIZE = 256
MAPWIDTH = 4
MAPHEIGHT = 3
WIN_LENGTH = MAPWIDTH * TILESIZE
WIN_HEIGHT = MAPHEIGHT * TILESIZE

GRID = [
    [space_tile for x in range(MAPWIDTH)] for y in range(MAPHEIGHT)
]

pygame.init()
pygame.display.set_caption("SpaceShooter_JDS")
WINDOW = pygame.display.set_mode((WIN_LENGTH, WIN_HEIGHT))
