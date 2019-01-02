import pygame
import random

from pathlib import PurePath


class Projectile:
    
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.move_count = 0
        self.vel = 10
        self.hitbox = (self.x_pos, self.y_pos, 1, 1)
    

class Bullet(Projectile):

    def __init__(self, x_pos, y_pos, radius, color, vel):
        super().__init__(x_pos, y_pos)

        self.radius = radius
        self.color = color
        self.vel = vel

    def draw(self, win):
        pygame.draw.circle(
            win, self.color, (self.x_pos, self.y_pos), self.radius
        )

        self.hitbox = (self.x_pos, self.y_pos, 1, 1)

        ### REMOVE THE VISIBLE HITBOX WHEN DONE
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        pass


class Meteor(Projectile):
    
    def __init__(self):
        x_pos = random.randint(0, 900)
        y_pos = 0

        meteor_options = [
            ["sprites\PNG\Meteors\meteorBrown_big1.png", 101, 84],
            ["sprites\PNG\Meteors\meteorBrown_big2.png", 120, 98],
            ["sprites\PNG\Meteors\meteorBrown_big3.png", 89, 82],
            ["sprites\PNG\Meteors\meteorBrown_big4.png", 98, 96],
        ]

        self.meteor_selection = random.choice(meteor_options)
        self.height = self.meteor_selection[2]
        self.width = self.meteor_selection[1]

        super().__init__(x_pos, y_pos - self.height)

        self.vel = random.randint(5, 10)
        
        self.hitbox = (self.x_pos, self.y_pos, self.width, self.height)
        self.image = pygame.image.load(self.meteor_selection[0])

    def draw(self, win):
        self.fall()
        win.blit(self.image, (self.x_pos, self.y_pos))
        self.hitbox = (self.x_pos, self.y_pos, self.width, self.height)

        ### REMOVE THE VISIBLE HITBOX WHEN DONE
        #pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)
    
    def fall(self):
        if self.y_pos < 800:
            self.y_pos += self.vel

    def check_hit(self, bullet):
        if bullet.y_pos - bullet.radius < self.hitbox[1] + self.hitbox[3] and bullet.y_pos + bullet.radius > self.hitbox[1]:
            if bullet.x_pos + bullet.radius > self.hitbox[0] and bullet.x_pos - bullet.radius < self.hitbox[0] + self.hitbox[2]:
                return True
            else:
                return False
        else:
            return False

    def hit(self):
        pass

