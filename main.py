import pygame
import math

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
BLACK = (0, 0, 0, 0)

class Player:
    x = 100
    y = 100
    rotation = 0
    velocity = 1
    lives = 3

    def __init__(self, x, y, rotation):
        self.x = x
        self.y = y
        self.rotation = rotation
        velocity = 1

class Asteroid:
    x = 50
    y = 50
    rotation = 90.0
    velocity = 1
    scale = 3 #lower by 1 each time hit and split into more asteroids, if at 1, dies when hit

    def __init__(self, x, y, rotation):
        self.x = x
        self.y = y
        self.rotation = rotation
        velocity = 1

def main():
    pygame.init()

    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    pygame.display.set_caption("Asteroids Genetic Algorithm")

    player = Player(100, 100, 0)
    ship = pygame.image.load("player.png")
    ship = pygame.transform.rotate(ship, -90)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.rotation += 15
        if keys[pygame.K_RIGHT]:
            player.rotation -= 15
        if keys[pygame.K_UP]:
            if player.velocity <= 50: player.velocity += 5
        if keys[pygame.K_DOWN]:
            if player.velocity >= 6: player.velocity -= 5

        #calculate new position.
        angle = math.radians(player.rotation)
        xcomp = math.cos(angle)
        ycomp = math.sin(angle)
        player.x += xcomp*player.velocity
        player.y -= ycomp*player.velocity
        
        #draw player
        rotatedShip = pygame.transform.rotate(ship, player.rotation)
        if player.y > WINDOW_HEIGHT: player.y -= WINDOW_HEIGHT
        if player.y < 0: player.y += WINDOW_HEIGHT
        if player.x > WINDOW_WIDTH: player.x -= WINDOW_WIDTH
        if player.x < 0: player.x += WINDOW_WIDTH
        win.fill(BLACK)
        win.blit(rotatedShip, (player.x, player.y))
        pygame.display.update()


    pygame.quit()

if __name__ == '__main__':
    main()
