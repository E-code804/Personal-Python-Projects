# Arrow Shooting Game

import pygame
import random

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 1416, 797
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Arrow Shooting")

# Loading images
player_arrow_ascend = pygame.transform.scale(pygame.image.load("PlayerArrowAscend.png"), (55,55))
player_arrow_descend = pygame.transform.scale(pygame.image.load("PlayerArrowDescend.png"), (55,55))
enemy_arrow_ascend = pygame.transform.scale(pygame.image.load("EnemyArrowAscend.png"), (55,55))
enemy_arrow_descend = pygame.transform.scale(pygame.image.load("EnemyArrowDescend.png"), (55,55))

player_avatar = pygame.transform.scale(pygame.image.load("Archers.png"), (200,200))
enemy_avatar = pygame.transform.scale(pygame.image.load("Archers2.png"), (200,200))

mountain_bg = pygame.transform.scale(pygame.image.load("MountainBG.png"), (WIDTH,HEIGHT))

# Defining the class for Arrow objects. Each Arrow has a start x and y
# coordinates, and a boolean determining if it is moving right
class Arrow:
    """docstring for Arrow."""

    def __init__(self, x, y, moveRight):
        #super(Arrow, self).__init__()
        self.x = x
        self.y = y
        self.moveRight = moveRight
        # If we are moving right, then the Arrow is a player Arrow. Enemy Arrow
        # if otherwise
        if moveRight:
            self.img = player_arrow_ascend
        else:
            self.img = enemy_arrow_ascend
    # Drawing the Arrows on the game window
    def draw(self, window):
        window.blit(self.img, (self.x, self.y))
    # Moving the arrows and using descendig arrows when reaches a certain x point.
    def move(self):
        mid = (WIDTH - self.x) / 2
        if self.moveRight:
            self.x += 5
            if self.x < mid:
                self.y -= 1
            else:
                self.img = player_arrow_descend
                self.y += 1
        # For enemy Arrows
        else:
            self.x -= 5
            if self.x > mid:
                self.y -= 1
            else:
                self.img = enemy_arrow_descend
                self.y += 1
# Defining the class for the Shooters objects. Each shooter has a starting x and
# y coordinate and a boolean determining if it is a player or not.
class Shooter:
    """docstring for Shooter."""

    def __init__(self, x, y, isPlayer):
        #super(Shooter, self).__init__()
        self.x = x
        self.y = y
        self.arrows = [] # Stores the arrows the Shooter shoots.
        self.cooldown_count = 20 # Cooldown between shots fired.
        self.isPlayer = isPlayer
        if isPlayer:
            self.img = player_avatar
        else:
            self.img = enemy_avatar

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, sign):
        self.x += (5 * sign)

    def cooldown(self):
        if self.cooldown_count >= 20:
            self.cooldown_count = 0
        elif self.cooldown_count > 0:
            self.cooldown_count += 1

    def shoot(self, arrow):
        self.cooldown()
        if self.cooldown_count == 0:
            self.arrows.append(arrow)
            self.cooldown_count = 1

def main():
    currentX, currentY = 750, 250
    arrowList = []
    playerStartingX, enemyStartingX, startingY = 0, 1216, 350
    player = Shooter(playerStartingX, startingY, True)
    enemy = Shooter(enemyStartingX, startingY, False)

    while True:
        win.blit(mountain_bg, (0,0))

        win.blit(enemy_avatar, (200,500))

        for arrow in player.arrows:
            arrow.draw(win)
            arrow.move()
            if arrow.x > (WIDTH - 20):
                player.arrows.remove(arrow)

        player.draw(win)
        enemy.draw(win)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.shoot(Arrow(player.x + 135, player.y + 15, True))
        if keys[pygame.K_d]:
            player.move(1)
        if keys[pygame.K_a]:
            player.move(-1)

main()
