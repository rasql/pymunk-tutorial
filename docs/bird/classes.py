import pygame
from pygame.locals import *

import pymunk
from pymunk.pygame_util import *
from pymunk import Vec2d
import math

# 30.4.2024 v1 : set this variable
pymunk.pygame_util.positive_y_is_up = True

pygame.init()
pygame.display.set_mode((200, 100))
screen = pygame.display.get_surface()

font = pygame.font.Font(None, 48)
WHITE = (255, 255, 255)

space = pymunk.Space()
space.gravity = 0, -900

draw_options = pymunk.pygame_util.DrawOptions(screen)

def post_solve_bird_pig(arbiter, space, _):
    bird, pig = arbiter.shapes
    space.remove(pig, pig.body)
    
    for obj in Game.objects:
        if obj.body == pig.body:
            Game.objects.remove(obj)

    Game.score += 10000


def post_solve_bird_wood(arbiter, space, _):
    bird, wood = arbiter.shapes
    
    if arbiter.total_impulse.length > 500:
        print(arbiter.total_impulse.length)
        space.remove(wood, wood.body)
        for obj in Game.objects:
            if obj.body == wood.body:
                Game.objects.remove(obj)

        Game.score += 5000


# type: 0=wood, 1=pig, 2=bird
space.add_collision_handler(2, 1).post_solve = post_solve_bird_pig
space.add_collision_handler(2, 0).post_solve = post_solve_bird_wood


class Object:
    def __init__(self, pos):
        self.body = pymunk.Body(1, 100)
        self.body.position = pos
        space.add(self.body)
        Game.objects.append(self)
        
    def draw(self):
        angle = self.body.angle
        img = pygame.transform.rotate(self.img, math.degrees(angle))
        
        pos = to_pygame(self.body.position, screen)
        rect = img.get_rect()
        rect.center = to_pygame(self.body.position, screen)
        screen.blit(img, rect)


class Circle(Object):
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
    
    def __init__(self, pos=(100, 100)):
        super().__init__(pos, type=1)


class Rectangle(Object):
    def __init__(self, pos):
        super().__init__(pos)
        size = self.img.get_size()
        shape = pymunk.Poly.create_box(self.body, size)
        shape.elasticity = 0
        shape.friction = 0.5
        space.add(shape)


class Beam(Rectangle):
    img = pygame.image.load('beam.png').convert_alpha()


class Column(Rectangle):
    img = pygame.image.load('column.png').convert_alpha()


class Game:
    objects = []
    level = 0
    score = 0
    debug = False
    
    def __init__(self):
        self.set_level(1)

    def draw_score(self):
        text = f'level {self.level} - score {self.score}'
        self.score_img = font.render(text, True, WHITE)
        screen.blit(self.score_img, (20, 20))
    
    def set_ground(self):
        shape = pymunk.Segment(space.static_body, (0, 10), (1200, 10), 4)
        shape.friction = 1
        shape.collision_type = 3
        space.add(shape)

    def remove_objects(self):
        """Remove all Objectects from space."""
        Game.objects = []
        for body in space.bodies:
            space.remove(body)
        for shape in space.shapes:
            space.remove(shape)
            
    def draw(self):
        """Draw pymunk Objectects on pygame screen."""
        if self.debug:
            space.debug_draw(draw_options)
        for obj in self.objects:
            obj.draw()
        self.draw_score()        

        space.step(0.02)
        
    def do_event(self, event):
        if event.type == KEYDOWN:
            if K_1 <= event.key <= K_9:
                i = int(event.unicode)
                self.set_level(i)
            
            if event.key == K_d:
                self.debug = not self.debug
                
    def launch_bird(self, p0, p1):
        """Get two sling points to launch the bird."""
        p0 = from_pygame(p0, screen)
        p1 = from_pygame(p1, screen)
        
        # 30.4.2024 v1 : add * to points p0, p1
        v = (Vec2d(*p0) - Vec2d(*p1)) * 10
        
        b = Bird(pos=p1)
        b.body.apply_impulse_at_local_point(v)
            
    def set_level(self, level):
        """Set player level."""
        self.level = level
        self.remove_objects()
        self.set_ground()

        if level == 1:
            Column((1000, 100))
            Column((1060, 100))
            Beam((1030, 145))
            Column((1000, 200))
            Column((1060, 200))
            Beam((1030, 245))
            Pig((1140, 60))

        elif level == 2:
            for i in range(2):
                Column((1000, 60 + i*100))
                Column((1060, 60 + i*100))
                Beam((1030, 105 + i*100))
            Pig((1000, 60))

        elif level == 3:
            for x in range(500, 800, 30):
                Column((x, 60))
            Pig((850, 60))

        elif level == 4:
            Column((500, 60))
            for x in range(500, 700, 85):
                Column((x+83, 60))
                Beam((x+40, 105))
                Pig((x+40, 50))

            Pig((850, 100))
