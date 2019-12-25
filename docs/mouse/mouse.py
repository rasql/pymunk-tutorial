import pymunk
from pymunk.pygame_util import *
from pymunk.vec2d import Vec2d

import pygame
from pygame.locals import *
import math
import random

space = pymunk.Space()
b0 = space.static_body
size = w, h = 700, 300

GRAY = (220, 220, 220)
RED = (255, 0, 0)


class Segment:
    def __init__(self, p0, v, radius=10):
        self.body = pymunk.Body()
        self.body.position = p0
        shape = pymunk.Segment(self.body, (0, 0), v, radius)
        shape.density = 0.1
        shape.elasticity = 0.5
        shape.filter = pymunk.ShapeFilter(group=1)
        shape.color = (0, 255, 0, 0)
        space.add(self.body, shape)


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
        pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for i in range(4):
            segment = pymunk.Segment(
                space.static_body, pts[i], pts[(i+1) % 4], d)
            segment.elasticity = 1
            segment.friction = 1
            space.add(segment)


class Poly:
    def __init__(self, pos, vertices):
        self.body = pymunk.Body(1, 100)
        self.body.position = pos

        shape = pymunk.Poly(self.body, vertices)
        shape.filter = pymunk.ShapeFilter(group=1)
        shape.density = 0.01
        shape.elasticity = 0.5
        shape.color = (255, 0, 0, 0)
        space.add(self.body, shape)


class Rectangle:
    def __init__(self, pos, size=(80, 50)):
        self.body = pymunk.Body()
        self.body.position = pos

        shape = pymunk.Poly.create_box(self.body, size)
        shape.density = 0.1
        shape.elasticity = 1
        shape.friction = 1
        space.add(self.body, shape)


class App:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(size)
        self.draw_options = DrawOptions(self.screen)
        self.active_shape = None
        self.pulling = False
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

            keys = {K_LEFT: (-1, 0), K_RIGHT: (1, 0),
                    K_UP: (0, 1), K_DOWN: (0, -1)}
            if event.key in keys:
                v = Vec2d(keys[event.key]) * 20
                if self.active_shape != None:
                    self.active_shape.body.position += v

        elif event.type == MOUSEBUTTONDOWN:
            p = from_pygame(event.pos, self.screen)
            self.active_shape = None
            for s in space.shapes:
                dist, info = s.point_query(p)
                if dist < 0:
                    self.active_shape = s
                    self.pulling = True

                    s.body.angle = (p - s.body.position).angle

        elif event.type == MOUSEMOTION:
            self.p = event.pos

        elif event.type == MOUSEBUTTONUP:
            if self.pulling:
                self.pulling = False
                b = self.active_shape.body
                p0 = Vec2d(b.position)
                p1 = from_pygame(event.pos, self.screen)
                impulse = 100 * Vec2d(p0 - p1).rotated(-b.angle)
                b.apply_impulse_at_local_point(impulse)

    def draw(self):
        self.screen.fill(GRAY)
        space.debug_draw(self.draw_options)

        if self.active_shape != None:
            s = self.active_shape
            r = int(s.radius)
            p = to_pygame(s.body.position, self.screen)
            pygame.draw.circle(self.screen, RED, p, r, 3)
            if self.pulling:
                pygame.draw.line(self.screen, RED, p, self.p, 3)
                pygame.draw.circle(self.screen, RED, self.p, r, 3)

        pygame.display.update()


if __name__ == '__main__':
    Box()

    r = 25
    for i in range(9):
        x = random.randint(r, w-r)
        y = random.randint(r, h-r)
        Circle((x, y), r)

    App().run()
