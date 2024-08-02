
import pygame
import numpy as np
import random
import time

class Boid():

    x_pos = 0
    y_pos = 0
    velocity = None
    acceleration = None

    def __init__(self):
        self.x_pos = random.randrange(0, 500)
        self.y_pos = random.randrange(0, 500)

        self.velocity = np.array([random.uniform(0, 1), random.uniform(0, 1)])
        self.acceleration = np.array([0, 0])
        

    def update(self):

        self.x_pos += self.velocity[0]
        self.y_pos += self.velocity[1]
        self.velocity += self.acceleration

        if self.x_pos < 0 or self.x_pos > 500:
            self.velocity[0] *= -1
        elif self.y_pos < 0 or self.y_pos > 500:
            self.velocity[1] *= -1

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