import pymunk
import pymunk.pygame_util
import pygame

pygame.init()
screen = pygame.display.set_mode((640, 240))
draw_options = pymunk.pygame_util.DrawOptions(screen)

space = pymunk.Space()
space.gravity = 0, -900

segment = pymunk.Segment(space.static_body, (20, 20), (400, 20), 1)
segment.elasticity = 0.95

body = pymunk.Body(mass=1, moment=10)
body.position = (100, 200)

circle = pymunk.Circle(body, radius=20)
circle.elasticity = 0.95
space.add(body, circle, segment)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.image.save(screen, 'intro1.png')

    screen.fill((200, 200, 200))
    space.debug_draw(draw_options)
    pygame.display.update()
    space.step(0.01)

pygame.quit()