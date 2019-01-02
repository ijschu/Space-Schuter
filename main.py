import pygame
import character
from grid import *
from items import *

clock = pygame.time.Clock()


def redrawGameWindow():
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            WINDOW.blit(GRID[row][column], (column * TILESIZE, row * TILESIZE))
    player.draw(WINDOW)
    for bullet in bullets:
        bullet.draw(WINDOW)
    for meteor in meteors:
        meteor.draw(WINDOW)
    pygame.display.update()

player = character.Player(500, 600, 98, 60)
bullets = []
bullet_cooldown = 0
meteors = []
GAME_OVER = False

### MAIN GAME LOOP ###
while not GAME_OVER:
    clock.tick(27)

    if bullet_cooldown > 0:
        bullet_cooldown += 1
    if bullet_cooldown > 3:
        bullet_cooldown = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_OVER = True

    for bullet in bullets:
        for meteor in meteors:
            if meteor.check_hit(bullet):
                meteor.hit()
                bullet.hit()
                bullets.pop(bullets.index(bullet))
                meteors.pop(meteors.index(meteor))
                break

    for meteor in meteors:
        if player.check_collision(meteor):
            player.meteor_collision()
            GAME_OVER = True
    
    for bullet in bullets:
        if bullet.y_pos > 0:
            bullet.y_pos -= bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    if len(meteors) < 7:
        meteors.append(
            Meteor()
        )

    for meteor in meteors:
        if meteor.y_pos < 800:
            meteor.y_pos += meteor.vel
        else:
            meteors.pop(meteors.index(meteor))

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and bullet_cooldown == 0:
        if len(bullets) < 10:
            bullets.append(
                Bullet(
                    player.x_pos + (player.width //2),
                    player.y_pos,
                    2,
                    (255,255,255),
                    player.vel + 5
                )
            )
        bullet_cooldown = 1

    if keys[pygame.K_LEFT] and player.x_pos > player.vel:
        player.x_pos -= player.vel
        left = True
        right = False
        up = False
        down = False
    elif keys[pygame.K_RIGHT] and player.x_pos < WIN_LENGTH - player.width - player.vel:
        player.x_pos += player.vel
        left = False
        right = True
        up = False
        down = False
    elif keys[pygame.K_UP] and player.y_pos > player.vel:
        player.y_pos -= player.vel
        left = False
        right = False
        up = True
        down = False
    elif keys[pygame.K_DOWN] and player.y_pos < WIN_HEIGHT - player.height - player.vel:
        player.y_pos += player.vel
        left = False
        right = False
        up = False
        down = True
    else:
        player.moveCount = 0
    
    redrawGameWindow()

pygame.quit()
