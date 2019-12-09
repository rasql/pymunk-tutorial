import pymunk
from pymunk import Vec2d
import pygame
import math

class Rectangle:
    def __init__(self, pos, file, space):
        self.img = pygame.image.load(file)
        size = self.img.get_size()

        moment = 1000
        mass = 5
        body = pymunk.Body(mass, moment)
        body.position = Vec2d(pos)
        shape = pymunk.Poly.create_box(body, size)
        shape.color = (0, 0, 255)
        shape.friction = 0.5
        shape.collision_type = 2
        space.add(body, shape)
        self.body = body
        self.shape = shape

    def draw(self):
        screen = pygame.display.get_surface()
        pos = self.body.position
        angle = self.body.angle

        img = pygame.transform.rotate(self.img, math.degrees(angle))
        w, h = img.get_size()
        x = pos[0] - w//2
        y = 600 - pos[1] - h//2
        screen.blit(img, (x, y))


class Polygon():
    def __init__(self, pos, length, height, space, mass=5.0):
        moment = 1000
        body = pymunk.Body(mass, moment)
        body.position = Vec2d(pos)
        shape = pymunk.Poly.create_box(body, (length, height))
        shape.color = (0, 0, 255)
        shape.friction = 0.5
        shape.collision_type = 2
        space.add(body, shape)
        self.body = body
        self.shape = shape
        wood = pygame.image.load("images/wood.png").convert_alpha()
        wood2 = pygame.image.load("images/wood2.png").convert_alpha()
        rect = pygame.Rect(251, 357, 86, 22)
        self.beam_image = wood.subsurface(rect).copy()
        rect = pygame.Rect(16, 252, 22, 84)
        self.column_image = wood2.subsurface(rect).copy()

    def to_pygame(self, p):
        """Convert pymunk to pygame coordinates"""
        return int(p.x), int(-p.y+600)

    def draw_poly(self, element, screen):
        """Draw beams and columns"""
        poly = self.shape
        ps = poly.get_vertices()
        ps.append(ps[0])
        ps = map(self.to_pygame, ps)
        ps = list(ps)
        color = (255, 0, 0)
        pygame.draw.lines(screen, color, False, ps)
        if element == 'beams':
            p = poly.body.position
            p = Vec2d(self.to_pygame(p))
            angle_degrees = math.degrees(poly.body.angle) + 180
            rotated_logo_img = pygame.transform.rotate(self.beam_image,
                                                       angle_degrees)
            offset = Vec2d(rotated_logo_img.get_size()) / 2.
            p = p - offset
            np = p
            screen.blit(rotated_logo_img, (np.x, np.y))
        if element == 'columns':
            p = poly.body.position
            p = Vec2d(self.to_pygame(p))
            angle_degrees = math.degrees(poly.body.angle) + 180
            rotated_logo_img = pygame.transform.rotate(self.column_image,
                                                       angle_degrees)
            offset = Vec2d(rotated_logo_img.get_size()) / 2.
            p = p - offset
            np = p
            screen.blit(rotated_logo_img, (np.x, np.y))

if __name__ == '__main__':
    pygame.init()
    size = (640, 480)
    pygame.display.set_mode(size)

    space = pymunk.Space()
    rect = Rectangle((100, 100), 'images/beam.png', space)
    rect.body.angle = 0.2
    rect.draw()
