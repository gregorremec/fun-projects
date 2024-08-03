# Gregor Remec - boids implementation with pygame
import pygame
import numpy as np
import random
import math

class Boid():

    x_pos = 0
    y_pos = 0
    velocity = None
    acceleration = None

    def __init__(self):
        self.x_pos = random.randrange(0, 500)
        self.y_pos = random.randrange(0, 500)

        self.velocity = np.array([random.uniform(0, 1), random.uniform(0, 1)])
        self.acceleration = np.array([random.uniform(0, 1), random.uniform(0, 1)])

    
    def distanceTo(self, other):

        p1 = (other.x_pos - self.x_pos)**2
        p2 = (other.y_pos - self.y_pos)**2
        return math.sqrt((p1 + p2))
        

    def update(self):


        self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]

        self.velocity += self.acceleration

        if self.velocity[0] > 1:
            self.velocity[0] = 1
        elif self.velocity[0] < -1:
            self.velocity[0] = -1

        if self.velocity[1] > 1:
            self.velocity[1] = 1
        elif self.velocity[1] < -1:
            self.velocity[1] = -1

        self.acceleration[0] *= .08
        self.acceleration[1] *= .08

        if self.x_pos < 0:
            self.x_pos = 500
        elif self.x_pos > 500:
            self.x_pos = 0
        if self.y_pos < 0:
            self.y_pos = 500
        elif self.y_pos > 500:
            self.y_pos = 0

        pygame.draw.circle(canvas, 0xffffff, (self.x_pos, self.y_pos), 4)




pygame.init()

canvas = pygame.display.set_mode((500, 500))

pygame.display.set_caption("FREAKING BOIDS")

exit = False

boid_list = []

for i in range(20):
    next_boid = Boid()
    boid_list.append(next_boid)

while not exit:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True

    canvas.fill((0, 0, 0))
        
    for boid in boid_list:
        boid.update()

    pygame.display.flip()
