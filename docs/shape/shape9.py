# pivot joint
from shape import pymunk, space, App, Box, Rectangle

b0 = space.static_body
p0 = 100, 200

body = pymunk.Body(mass=1, moment=10)
body.position = (100, 50)
circle = pymunk.Circle(body, radius=30)

joint = pymunk.constraint.DampedSpring(b0, body, p0, (0, 0), 100, 100, 0)
space.add(body, circle, joint)

App().run()