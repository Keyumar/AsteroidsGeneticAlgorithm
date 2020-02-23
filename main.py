import pygame
import math

class Player:
    x = 50
    y = 50
    rotation = 90
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

    win = pygame.display.set_mode((800, 600))

    pygame.display.set_caption("Asteroids Genetic Algorithm")

    player = Player(50, 50, 90)
    ship = pygame.image.load("player.png")

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            player.rotation -= 0.3
        if keys[pygame.K_RIGHT]:
            player.rotation += 0.3
        if keys[pygame.K_UP]:
            player.y -= math.sin(player.rotation)
            player.x += math.cos(player.rotation)
        if keys[pygame.K_DOWN]:
            player.y += player.velocity

        win.fill((0, 0, 0, 0))

        #draw player
        playerRotation = pygame.transform.rotate(ship, player.rotation)
        win.blit(playerRotation, (player.x, player.y))
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
