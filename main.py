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
    IMAGE = "player.png"

    def __init__(self, x, y, rotation):
        self.x = x
        self.y = y
        self.rotation = rotation
        velocity = 1

class Projectile:
    x = 100
    y = 100
    rotation = 0
    velocity = 5

    def __init__(self, x, y, rotation):
        self.x = x
        self.y = y
        self.rotation = rotation
        velocity = 5

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
    ship = pygame.image.load(player.IMAGE)
    ship = pygame.transform.rotate(ship, -90)

    projectiles = []

    timer =  pygame.time.Clock()

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
        if keys[pygame.K_SPACE]:
            projectiles.append(fireProjectile(player, ship))

        win.fill(BLACK)

        #calculate and draw projectiles
        for each in projectiles:
            each.x += math.cos(math.radians(each.rotation))*each.velocity
            each.y -= math.sin(math.radians(each.rotation))*each.velocity
            pygame.draw.line(win, (255, 255, 255), (each.x, each.y), (each.x, each.y))

        #calculate new ship position.
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
        newship = rotatedShip.get_rect(center = ship.get_rect(topleft = (player.x, player.y)).center)
        win.blit(rotatedShip, newship.topleft)

        pygame.display.update()
        timer.tick(60)

    pygame.quit()

def fireProjectile(player, ship):
    x = player.x + ship.get_rect().centerx
    y = player. y + ship.get_rect().centery
    fire = Projectile(x, y, player.rotation)
    return fire

if __name__ == '__main__':
    main()
