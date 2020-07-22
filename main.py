import pygame

WIDTH = 511
HEIGHT = 511

pygame.init()
game = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

class Airplane:
    MOVE_RIGHT = 0
    MOVE_LEFT = 1
    MOVE_DOWN = 2
    MOVE_UP = 3

    def __init__(self, start):
        self.img = pygame.image.load("./resource/plane.png")
        self.img = pygame.transform.scale(self.img, (WIDTH//7,  HEIGHT//7))
        _, _, self.W, self.H = self.img.get_rect()
        self.x, self.y = start
        self.x *= self.W
        self.y *= self.H

    def draw(self, game):
        game.blit(self.img, (self.x, self.y))

    def goto(self, position):
        self.x, self.y = position
        self.x *= self.W
        self.y *= self.H

    def move(self, direction):
        if direction == Airplane.MOVE_RIGHT:
            self.x += self.W
        elif direction == Airplane.MOVE_LEFT:
            self.x -= self.W
        elif direction == Airplane.MOVE_DOWN:
            self.y += self.H
        elif direction == Airplane.MOVE_UP:
            self.y -= self.H

    def __eq__(self, other):
        if other.x == self.x and other.y == self.y:
            return True
        else:
            return False

class Bat:
    def __init__(self, start):
        self.img = pygame.image.load("./resource/bat.png")
        self.img = pygame.transform.scale(self.img, (WIDTH//7,  HEIGHT//7))
        _, _, self.W, self.H = self.img.get_rect()
        self.x, self.y = start
        self.x *= self.W
        self.y *= self.H

    def draw(self, game):
        game.blit(self.img, (self.x, self.y))

class Fire:
    def __init__(self, start):
        self.img = pygame.image.load("./resource/boom.png")
        self.img = pygame.transform.scale(self.img, (WIDTH//7,  HEIGHT//7))
        _, _, self.W, self.H = self.img.get_rect()
        self.x, self.y = start
        self.x *= self.W
        self.y *= self.H

    def draw(self, game):
        game.blit(self.img, (self.x, self.y))

class FireManager:
    def __init__(self):
        self.fires = []

    def drawAll(self, game):
        for fire in self.fires:
            fire.draw(game)

    def newFire(self, start):
        self.fires.append(Fire(start))

from maze import MazeSolver
solver = MazeSolver('mazeTest3.txt')
start, end, walls = solver.getMaze()
player = Airplane(start)
goal = Bat(end)

fm = FireManager()
for wall in walls:
    fm.newFire(wall)

pathHelper = solver.findPath()

# pathHelper = solver.getPath()
crashed = False
while not crashed:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            crashed = True
        if e.type == pygame.KEYUP:
            player.goto(next(pathHelper))
    game.fill((255, 255, 255))
    player.draw(game)
    goal.draw(game)

    if player == goal:
        crashed = True

    fm.drawAll(game)
    pygame.display.update()
    clock.tick(60)

pygame.quit()