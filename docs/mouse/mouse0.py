import pymunk
from pymunk.pygame_util import *
from pymunk.vec2d import Vec2d

import pygame
from pygame.locals import *
import random

space = pymunk.Space()
b0 = space.static_body
size = w, h = 700, 300

GRAY = (220, 220, 220)
RED = (255, 0, 0)


class Circle:
    def __init__(self, pos, radius=20):
        self.body = pymunk.Body()
        self.body.position = pos
        shape = pymunk.Circle(self.body, radius)
        shape.density = 0.01
        shape.friction = 0.9
        shape.elasticity = 1
        space.add(self.body, shape)


class Box:
    def __init__(self, p0=(0, 0), p1=(w, h), d=4):
        x0, y0 = p0
        x1, y1 = p1
        ps = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for i in range(4):
            segment = pymunk.Segment(b0, ps[i], ps[(i+1) % 4], d)
            segment.elasticity = 1
            segment.friction = 1
            space.add(segment)


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.draw_options = DrawOptions(self.screen)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                self.do_event(event)
            self.draw()
            space.step(0.01)

        pygame.quit()

    def do_event(self, event):
        if event.type == QUIT:
            self.running = False

        elif event.type == KEYDOWN:
            if event.key in (K_q, K_ESCAPE):
                self.running = False

            if event.key == K_p:
                pygame.image.save(self.screen, 'mouse.png')

    def draw(self):
        self.screen.fill(GRAY)
        space.debug_draw(self.draw_options)
        pygame.display.update()


if __name__ == '__main__':
    Box()
    App().run()
