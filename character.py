import pygame

ship_sprite = "sprites\PNG\playerShip3_red.png"

MOVES = {
    "Left": [pygame.image.load(ship_sprite), ],
    "Right": [pygame.image.load(ship_sprite), ],
    "Up": [pygame.image.load(ship_sprite), ],
    "Down": [pygame.image.load(ship_sprite), ]
}

char = pygame.image.load(ship_sprite)

class Character:
    def __init__(self, x_pos, y_pos, width, height):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self.vel = 5
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.moveCount = 0

    def draw(self, win):
        if self.moveCount + 1 >= 27:
            self.moveCount = 0
        
        if self.left:
            win.blit(MOVES["Left"][self.moveCount//3], (self.x_pos, self.y_pos))
            self.moveCount += 1
        elif self.right:
            win.blit(MOVES["Right"][self.moveCount//3], (self.x_pos, self.y_pos))
            self.moveCount += 1
        elif self.up:
            win.blit(MOVES["Up"][self.moveCount//3], (self.x_pos, self.y_pos))
            self.moveCount += 1
        elif self.down:
            win.blit(MOVES["Down"][self.moveCount//3], (self.x_pos, self.y_pos))
            self.moveCount += 1
        else:
            win.blit(char, (self.x_pos, self.y_pos))


class Player(Character):

    def __init__(self, x_pos, y_pos, width, height):
        super().__init__(x_pos, y_pos, width, height)

        self.hitbox = (self.x_pos, self.y_pos, width, height)
        self.vel = 30

    def draw(self, win):
        if self.moveCount + 1 >= 27:
            self.moveCount = 0

        if self.left:
            win.blit(MOVES["Left"][self.moveCount//3], (self.x_pos, self.y_pos))
            self.moveCount += 1
        elif self.right:
            win.blit(MOVES["Right"][self.moveCount//3], (self.x_pos, self.y_pos))
            self.moveCount += 1
        elif self.up:
            win.blit(MOVES["Up"][self.moveCount//3], (self.x_pos, self.y_pos))
            self.moveCount += 1
        elif self.down:
            win.blit(MOVES["Down"][self.moveCount//3], (self.x_pos, self.y_pos))
            self.moveCount += 1
        else:
            win.blit(char, (self.x_pos, self.y_pos))

        self.hitbox = (self.x_pos, self.y_pos, 98, 60)

        ### REMOVE THE VISIBLE HITBOX WHEN DONE
        #pygame.draw.rect(win, (255,0,0), self.hitbox, 2)

    def check_collision(self, meteor):
        # Check for front collision
        if meteor.y_pos + meteor.height > self.hitbox[1] and meteor.y_pos + meteor.height < self.hitbox[1] + self.hitbox[3]:
            if meteor.x_pos + meteor.width > self.hitbox[0] and meteor.x_pos < self.hitbox[0] + self.hitbox[2]:
                front_collision = True
            else:
                front_collision = False
        else:
            front_collision = False

        # Check for rear collision
        if self.hitbox[1] + self.hitbox[3] > meteor.y_pos and self.hitbox[1] + self.hitbox[3] < meteor.y_pos + meteor.height:
            if self.hitbox[0] + self.hitbox[2] > meteor.x_pos and self.hitbox[0] < meteor.x_pos + meteor.width:
                rear_collision = True
            else:
                rear_collision = False
        else:
            rear_collision = False
        
        return True if front_collision == True or rear_collision == True else False

    def meteor_collision(self):
        print("WE'VE BEEN HIT!")
