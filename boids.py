# Gregor Remec - boids implementation with pygame
import pygame
import numpy as np
import random
import math

SCREEN_SIZE = 700

class Boid():

    position = None
    velocity = None
    acceleration = None

    def __init__(self):

        self.position = np.array([float(random.randrange(0, SCREEN_SIZE)), float(random.randrange(0, SCREEN_SIZE))])
        self.velocity = np.array([random.uniform(0, 1), random.uniform(0, 1)])
        self.acceleration = np.array([random.uniform(0, 1), random.uniform(0, 1)])

    
    def distanceTo(self, other):

        p1 = (other.position[0] - self.position[1])**2
        p2 = (other.position[0] - self.position[1])**2
        return math.sqrt((p1 + p2))
    
    def align(self, flock):

        steeringForce = np.array([0.0,0.0])

        for boid in flock:
            steeringForce += boid.velocity

        return steeringForce / len(flock)

    def update(self, flock):

        self.acceleration = self.align(flock)
        self.position += self.velocity
        self.velocity += self.acceleration

        if self.velocity[0] > 1:
            self.velocity[0] = 1
        elif self.velocity[0] < -1:
            self.velocity[0] = -1

        if self.velocity[1] > 1:
            self.velocity[1] = 1
        elif self.velocity[1] < -1:
            self.velocity[1] = -1

        if self.position[0] < 0:
            self.position[0] = SCREEN_SIZE
        elif self.position[0] > SCREEN_SIZE:
            self.position[0] = 0
        if self.position[1] < 0:
            self.position[1] = SCREEN_SIZE
        elif self.position[1] > SCREEN_SIZE:
            self.position[1] = 0

        pygame.draw.circle(canvas, 0xffffff, (self.position[0], self.position[1]), 4)




pygame.init()

canvas = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

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
        boid.update(boid_list)

    pygame.display.flip()
