import pygame
from pygame.locals import *

import pymunk
from pymunk.pygame_util import *
from pymunk import Vec2d
import math

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
size = 1200, 600
screen = pygame.display.set_mode(size)
font = pygame.font.Font(None, 48)

background = pygame.image.load('background.png').convert_alpha()
bird = pygame.image.load('bird.png').convert_alpha()
sling = pygame.image.load('sling.png').convert_alpha()
sling2 = pygame.image.load('sling2.png').convert_alpha()

pygame.mixer.music.load('angry-birds.ogg')
pygame.mixer.music.play(-1)

objects = []

class Obj:
    def __init__(self, pos, angle=0):
        self.body = pymunk.Body(1, 100)
        self.body.position = pos
        self.body.angle = math.radians(angle)
        space.add(self.body)
        objects.append(self)
        
    def draw(self):
        angle = self.body.angle
        img = pygame.transform.rotate(self.img, math.degrees(angle))
        
        pos = to_pygame(self.body.position, screen)
        rect = img.get_rect()
        rect.center = to_pygame(self.body.position, screen)
        screen.blit(img, rect)

class Circle(Obj):
    def __init__(self, pos, type=0):
        super().__init__(pos)
        shape = pymunk.Circle(self.body, 32)
        shape.elasticity = 0.5
        shape.friction = 0.5
        shape.collision_type = type
        space.add(shape)

class Bird(Circle):
    img = pygame.image.load('bird.png').convert_alpha()

    def __init__(self, pos):
        super().__init__(pos, type=2)

class Pig(Circle):
    img = pygame.image.load('pig.png').convert_alpha()
    img = pygame.transform.scale(img, (64, 64))
    
    def __init__(self, pos):
        super().__init__(pos, type=1)

class Disc(Circle):
    img = pygame.image.load('disc.png').convert_alpha()
    img = pygame.transform.scale(img, (64, 64))

class Rectangle(Obj):
    def __init__(self, pos):
        super().__init__(pos)
        size = self.img.get_size()
        shape = pymunk.Poly.create_box(self.body, size)
        shape.elasticity = 0.1
        shape.friction = 0.99
        space.add(shape)

class Beam(Rectangle):
    img = pygame.image.load('beam.png').convert_alpha()

class Column(Rectangle):
    img = pygame.image.load('column.png').convert_alpha()


class Triangle(Obj):
    img = pygame.image.load('triangle.png').convert_alpha()
    size = img.get_size()
    w, h = size
    vertices = [(-w//2, -h//2), (w//2, -h//2), (0, h//2)]

    def __init__(self, pos, angle=0):
        super().__init__(pos, angle)
        shape = pymunk.Poly(self.body, self.vertices)
        space.friction = 1
        space.add(shape)

class Level:
    def __init__(self):
        self.score = 0
        self.set(1)

    def render(self):
        text = f'level {self.level} - score {self.score}'
        self.img = font.render(text, True, WHITE)
    
    def draw(self):
        screen.blit(self.img, (20, 20))

    def set_ground(self):
        shape = pymunk.Segment(space.static_body, (0, 10), (1200, 10), 4)
        shape.friction = 1
        space.add(shape)

    def remove_objects(self):
        """Remove all objects from space."""
        global objects
        objects = []
        for body in space.bodies:
            space.remove(body)
        for shape in space.shapes:
            space.remove(shape)

    def set(self, level):
        """Set player level."""
        self.level = level
        self.render()

        self.remove_objects()
        self.set_ground()

        if level == 1:
            Triangle((600, 60))
            Triangle((700, 60))
            Pig((800, 60))

            Column((1000, 100))
            Column((1060, 100))
            Beam((1030, 145))
            Column((1000, 200))
            Column((1060, 200))
            Beam((1030, 245))

            Pig((1140, 60))

        elif level == 2:
            Column((1000, 100))
            Column((1000, 200))
            Pig((1100, 60))

        elif level == 3:
            Triangle((500, 60))
            Triangle((590, 60))
            Pig((700, 100))

        elif level == 4:
            Triangle((500, 60))
            Triangle((590, 60))
            Triangle((680, 60))
            Pig((750, 100))

        else:
            print('level not implemented')


def post_solve_bird_pig(arbiter, space, _):
    print(arbiter)
    bird, pig = arbiter.shapes
    pig.body

    space.remove(pig, pig.body)
    for obj in objects:
        if obj.body == pig.body:
            objects.remove(obj)

    level.score += 10000
    level.render()
    level.set(level.level+1)

space = pymunk.Space()
space.gravity = 0, -900
draw_options = pymunk.pygame_util.DrawOptions(screen)
space.add_collision_handler(2, 1).post_solve=post_solve_bird_pig

bird_rect0 = Rect(160, 380, 100, 100)
bird_rect = bird_rect0.copy()
sling1_pos = (220, 415)
sling2_pos = (173, 415)

running = True
stepping = True
shooting = False
debugging = False

level = Level()

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key in (K_q, K_ESCAPE):
                running = False

            if event.key == K_s:
                stepping = not stepping

            if event.key == K_d:
                debugging = not debugging

            if K_1 <= event.key <= K_9:
                i = int(event.unicode)
                level.set(i)

        if event.type == MOUSEBUTTONDOWN:
            print(from_pygame(event.pos, screen))
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
                b = Bird(pos=p0)
                b.body.apply_impulse_at_local_point(v)

    screen.blit(background, (0, 0))
    if debugging:
        space.debug_draw(draw_options)
    screen.blit(sling, (200, 380))
    for object in objects:
        object.draw()

    p0 = bird_rect.move(10, 40).topleft
    pygame.draw.line(screen, BLACK, sling1_pos, p0, 4)
    screen.blit(bird, bird_rect)
    pygame.draw.line(screen, BLACK, sling2_pos, p0, 4)
    screen.blit(sling2, (170, 380))

    level.draw()
    pygame.display.update()
    
    if stepping:
        space.step(0.02)

pygame.quit()