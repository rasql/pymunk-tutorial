import pymunk
from pymunk.pygame_util import *
from pymunk import Vec2d

import pygame
from pygame.locals import *

import math, random

width, height = 600, 600
fps = 60
dt = 1./fps
pygame.init()

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 16)

draw_options = pymunk.pygame_util.DrawOptions(screen)
space = pymunk.Space()
b0 = space.static_body

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTGRAY = (220, 220, 220)

objects = []

class App:
    def __init__(self):
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == QUIT: 
                    self.running = False
                
                elif event.type == KEYDOWN:
                    if event.key in (K_q, K_ESCAPE):
                        self.running = False

            self.draw()
            clock.tick(fps)
            space.step(1/fps)

        pygame.quit()

    def draw(self):
        screen.fill(BLACK)
        space.debug_draw(draw_options)

        for obj in objects:
            obj.draw()

        pygame.display.update()


class Text:
    def __init__(self, text='Text', pos=(0, 0), color=WHITE):
        self.rect = Rect(*pos, 0, 0)
        self.color = color
        self.set(text)
        objects.append(self)

    def set(self, text):
        self.text = text
        self.render()

    def render(self):
        self.img = font.render(self.text, True, self.color)
        self.rect.size = self.img.get_size()

    def draw(self):
        screen.blit(self.img, self.rect)

class Obj:
    """pymunk object with inheritable options"""
    pass

class Circle:
    def __init__(self, pos, radius):
        self.body = pymunk.Body()
        self.body.position = pos
        self.shape = pymunk.Circle(self.body, radius)
        self.shape.density = 0.1
        space.add(self.body, self.shape)


class Segment:
    def __init__(self, p, *args, d=2, color=None, friction=1):
        p = Vec2d(p)
        for v in args:
            shape = pymunk.Segment(b0, p, p+v, d)
            shape.color = LIGHTGRAY
            shape.elasticity = 1
            shape.friction = friction
            if color != None:
                shape.color = color
            p = p + v
            space.add(shape)

class Poly:
    def __init__(self, pos, vs, img):
        self.body = pymunk.Body()
        self.body.position = pos
        shape = pymunk.Poly(self.body, vs)
        shape.density = 0.01
        shape.friction = 0.5    
        space.add(self.body, shape)
        objects.append(self)
        self.img = img

    def draw(self):
        pos = to_pygame(self.body.position, screen)
        angle = math.degrees(self.body.angle) + 180
        img = pygame.transform.rotate(self.img, angle)
        rect = img.get_rect()
        rect.center = pos
        screen.blit(img, rect)
        pygame.draw.circle(screen, YELLOW, pos, 5)

if __name__ == '__main__':
    Text(f'Version: {pymunk.version}', (50, 5))
    Text(f'Chipmunk version: {pymunk.chipmunk_version}', (50, 20))
    Text('Demo Lib', (50, 35))

    Circle((100, 200), 30)

    space.gravity = 0, -1000

    b = pymunk.Body(1, 100)
    s = pymunk.Circle(b, 20)
    s.collision_type = 100
    print(b, s, s.collision_type)

    h0 = space.add_default_collision_handler()
    print(h0)

    h = space.add_collision_handler(1, 99)
    print(h)

    Text(f'Version: {pymunk.version}', (50, 5))
    Text(f'Chipmunk version: {pymunk.chipmunk_version}', (50, 20))
    Text('Demo Lib', (50, 35))

    p0 = 50, 50
    Segment(p0, (500, 0), (0, 500), (-500, 0), (0, -500))

    c = Circle((100, 200), 30)
    c.shape.color = GREEN
    c = Circle((200, 200), 20)
    c.body.body_type = pymunk.Body.KINEMATIC

    c = Circle((300, 200), 20)
    c.body.body_type = pymunk.Body.STATIC

    App().run()