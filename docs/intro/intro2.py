from intro import pymunk, space, App

segment = pymunk.Segment(space.static_body, (20, 120), (400, 20), 1)
segment.elasticity = 0.5
segment.friction = 0.5

body = pymunk.Body(mass=1, moment=10)
body.position = (100, 200)

circle = pymunk.Circle(body, radius=20)
circle.elasticty = 0.5
circle.friction = 0.5
space.add(body, circle, segment)

App().run()