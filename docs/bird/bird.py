import pygame
from pygame.locals import *

import pymunk
import pymunk.pygame_util
from pymunk import Vec2d

import math

BLACK = (0, 0, 0)

pygame.init()
size = 1200, 600
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 72)
score = font.render('score', True, BLACK)

background = pygame.image.load('background.png').convert_alpha()
bird = pygame.image.load('bird.png').convert_alpha()
pig = pygame.image.load('pig.png').convert_alpha()
beam = pygame.image.load('beam.png').convert_alpha()
sling = pygame.image.load('sling.png').convert_alpha()
sling2 = pygame.image.load('sling2.png').convert_alpha()

pygame.mixer.music.load('angry-birds.ogg')
pygame.mixer.music.play(-1)

objects = []

class Obj:
    def draw(self):
        pos = self.body.position
        angle = self.body.angle

        img = pygame.transform.rotate(self.img, math.degrees(angle))
        w, h = img.get_size()
        x = pos[0] - w//2
        y = 600 - pos[1] - h//2
        screen.blit(img, (x, y))

class Circle(Obj):
    def __init__(self, pos, radius=10, img=None):
        body = pymunk.Body(1, 1)
        body.position = pos
        shape = pymunk.Circle(body, 32)
        shape.elasticity = 0.5
        space.add(body, shape)
        self.body = body
        self.img = bird

        objects.append(self)

class Rectangle(Obj):
    def __init__(self, pos, size, angle=0):
        self.img = beam
        size = self.img.get_size()

        body = pymunk.Body()
        body.position = pos
        body.angle = angle
        shape = pymunk.Poly.create_box(body, size)
        shape.density = 0.01
        shape.elasticity = 0.5
        space.add(body, shape)
        self.body = body

        objects.append(self)
        


space = pymunk.Space()
space.gravity = 0, -900
draw_options = pymunk.pygame_util.DrawOptions(screen)

shape = pymunk.Segment(space.static_body, (0, 20), (1200, 20), 2)
shape.elasticity = 0.95
shape.friction = 1
space.add(shape)

Rectangle ((1000, 100), (40, 120))
Rectangle ((1000, 200), (40, 120), angle=90)

bird_rect0 = Rect(160, 380, 100, 100)
bird_rect = bird_rect0.copy()
sling1_pos = (220, 415)
sling2_pos = (173, 415)

running = True
stepping = True
shooting = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key in (K_q, K_ESCAPE):
                running = False

            if event.key == K_s:
                stepping = not stepping

        if event.type == MOUSEBUTTONDOWN:
            print(event.pos)
            if bird_rect.collidepoint(event.pos):
                shooting = True

        if event.type == MOUSEMOTION:
            if shooting:
                bird_rect.move_ip(event.rel)

        if event.type == MOUSEBUTTONUP:
            if shooting:
                shooting = False
                bird_rect = bird_rect0.copy()
                p0 = pymunk.pygame_util.from_pygame(event.pos, screen)
                p1 = pymunk.pygame_util.from_pygame(sling1_pos, screen)
                v = (Vec2d(p1) - Vec2d(p0)) * 10
                print(v)
                b = Circle(pos=p0)
                b.body.apply_impulse_at_local_point(v)

    screen.blit(background, (0, 0))
    # space.debug_draw(draw_options)

    screen.blit(sling, (200, 380))

    for object in objects:
        object.draw()

    p0 = bird_rect.move(10, 40).topleft
    pygame.draw.line(screen, BLACK, sling1_pos, p0, 4)
    screen.blit(bird, bird_rect)
    pygame.draw.line(screen, BLACK, sling2_pos, p0, 4)
    screen.blit(sling2, (170, 380))

    screen.blit(score, (20, 20))
    
    pygame.display.update()
    
    if stepping:
        space.step(0.01)

pygame.quit()