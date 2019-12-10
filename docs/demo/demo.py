import pygame
from pygame.locals import *
import pymunk
import pymunk.pygame_util
import random

width, height = 600, 500

class Ball:
    """Create a ball object in Pymunk."""
    def __init__(self, mass, pos, radius, space):
        self.space = space
        self.mass = mass
        self.pos = pos
        self.radius = radius
        self.intertia = pymunk.moment_for_circle(mass, 0, radius, (0, 0))
        
        # calculate mass and inertia from shape density
        body = pymunk.Body()
        body.position = pos
        shape = pymunk.Circle(body, radius)
        shape.density = 1
        space.add(body, shape)

        self.body = body
        self.shape = shape

    def kill(self):
        self.space.remove(self.body, self.shape)

def add_ball(space):
    """Add a ball to the given space at a random position"""
    mass = 1
    radius = 24
    inertia = pymunk.moment_for_circle(mass, 0, radius, (0,0))
    body = pymunk.Body(mass, inertia)
    x = random.randint(120,380)
    body.position = x, height-50
    shape = pymunk.Circle(body, radius, (0,0))
    space.add(body, shape)
    return shape

def add_L(space):
    """Add a inverted L shape with two joints"""
    rotation_center_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    rotation_center_body.position = (300,300)

    rotation_limit_body = pymunk.Body(body_type = pymunk.Body.STATIC)
    rotation_limit_body.position = (200,300)

    body = pymunk.Body(10, 10000)
    body.position = (300,300)
    l1 = pymunk.Segment(body, (-150, 0), (255.0, 0.0), 5.0)
    l2 = pymunk.Segment(body, (-150.0, 0), (-150.0, 50.0), 5.0)

    rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0,0), (0,0))
    joint_limit = 25
    rotation_limit_joint = pymunk.SlideJoint(body, rotation_limit_body, (-100,0), (0,0), 0, joint_limit)

    space.add(l1, l2, body, rotation_center_joint, rotation_limit_joint)
    return l1,l2

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()

    space = pymunk.Space()
    space.gravity = (0.0, -900.0)

    lines = add_L(space)
    balls = []
    balls2 = []
    draw_options = pymunk.pygame_util.DrawOptions(screen)

    ticks_to_next_ball = 10

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        ticks_to_next_ball -= 1
        if ticks_to_next_ball <= 0:
            ticks_to_next_ball = 25
            ball_shape = add_ball(space)
            balls.append(ball_shape)

            d = 50
            pos = random.randint(d, width-d), height-d
            balls2.append(Ball(0, pos, 15, space))

        screen.fill((255,255,255))

        balls_to_remove = []
        for ball in balls:
            if ball.body.position.y < 150:
                balls_to_remove.append(ball)

        for ball in balls_to_remove:
            space.remove(ball, ball.body)
            balls.remove(ball)

        for b in balls2[:]:
            if b.body.position.y < 50:
                b.kill()
                balls2.remove(b)

        space.debug_draw(draw_options)

        space.step(1/50.0)

        pygame.display.flip()
        clock.tick(50)

    pygame.quit()

if __name__ == '__main__':
    main()