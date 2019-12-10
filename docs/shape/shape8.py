# pivot joint
from shape import pymunk, space, App, Box, Rectangle

b0 = space.static_body

body = pymunk.Body(mass=1, moment=10)
body.position = (100, 200)
circle = pymunk.Circle(body, radius=50)

joint = pymunk.constraint.PivotJoint(b0, body, (200, 200))
space.add(body, circle, joint)

App().run()