# conveyer belt using surface velocity
from shape import pymunk, space, App, Box, Rectangle

b0 = space.static_body
shape = pymunk.Segment(b0, (20, 20), (500, 150), 10)
shape.friction = 1
shape.surface_velocity = (100, 100)
space.add(shape)

Rectangle((100, 200))
App().run()