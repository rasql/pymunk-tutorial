from intro import pymunk, space, App
from random import randint

pts = [(10, 10), (690, 10), (690, 230), (10, 230)]
for i in range(4):
    seg = pymunk.Segment(space.static_body, pts[i], pts[(i+1)%4], 2)
    seg.elasticity = 0.999
    space.add(seg)

space.gravity = 0, 0
for i in range(40):
    body = pymunk.Body(mass=1, moment=10)
    body.position = randint(40, 660), randint(40, 200)
    impulse = randint(-100, 100), randint(-100, 100)       
    body.apply_impulse_at_local_point(impulse)
    circle = pymunk.Circle(body, radius=10)
    circle.elasticity = 0.999
    circle.friction = 0.5
    space.add(body, circle)

App().run()