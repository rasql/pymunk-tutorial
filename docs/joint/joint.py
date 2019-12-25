import pymunk
import pymunk.pygame_util
from pymunk.vec2d import Vec2d

import pygame
import math

space = pymunk.Space()
space.gravity = 0, -900
b0 = space.static_body

class PinJoint:
    def __init__(self, a, b, anchor_a=(0, 0), anchor_b=(0, 0)):
        joint = pymunk.constraint.PinJoint(a, b, anchor_a, anchor_b)
        space.add(joint)

class PivotJoint:
    def __init__(self, a, b, anchor_a=(0, 0), anchor_b=(0, 0)):
        joint = pymunk.constraint.PinJoint(a, b, anchor_a, anchor_b)
        joint.collide_bodies = False
        space.add(joint)

class GrooveJoint:
    def __init__(self, a, b, groove_a, groove_b, anchor_b):
        joint = pymunk.constraint.GrooveJoint(a, b, groove_a, groove_b, anchor_b)
        joint.collide_bodies = False
        space.add(joint)

class DampedRotarySpring:
    def __init__(self, a, b, rest_angle, stiffness, damping):
        joint = pymunk.constraint.DampedRotarySpring(a, b, rest_angle, stiffness, damping)
        space.add(joint)

class RotaryLimitJoint:
    def __init__(self, a, b, min, max, collide=True):
        joint = pymunk.constraint.RotaryLimitJoint(a, b, min, max)
        joint.collide_bodies = collide
        space.add(joint)


class RatchetJoint:
    def __init__(self, a, b, phase, ratchet):
        joint = pymunk.constraint.GearJoint(a, b, phase, ratchet)
        space.add(joint)
class SimpleMotor:
    def __init__(self, a, b, rate):
        joint = pymunk.constraint.SimpleMotor(a, b, rate)
        space.add(joint)

class GearJoint:
    def __init__(self, a, b, phase, ratio):
        joint = pymunk.constraint.GearJoint(a, b, phase, ratio)
        space.add(joint)

def info(body):
    print(f'm={body.mass:.0f} moment={body.moment:.0f}')
    cg = body.center_of_gravity
    print(cg.x, cg.y)

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
        space.add(self.body, shape)

class Box:
    def __init__(self, p0=(10, 10), p1=(690, 230), d=2):
        x0, y0 = p0
        x1, y1 = p1
        pts = [(x0, y0), (x1, y0), (x1, y1), (x0, y1)]
        for i in range(4):
            segment = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%4], d)
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
        self.screen = pygame.display.set_mode((700, 240))
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.image.save(self.screen, 'joint.png')

            self.screen.fill((220, 220, 220))
            space.debug_draw(self.draw_options)
            pygame.display.update()
            space.step(0.01)

        pygame.quit()

if __name__ == '__main__':
    Box()

    body = pymunk.Body(mass=1, moment=10)
    body.position = (100, 200)
    body.apply_impulse_at_local_point((200, 0))

    circle = pymunk.Circle(body, radius=20)
    circle.elasticity = 0.95
    circle.friction = 1
    space.add(body, circle)

    info(body)
    App().run()