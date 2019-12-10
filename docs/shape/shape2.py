from shape import pymunk, space, App, Box

Box()
body = pymunk.Body(mass=1, moment=1000)
body.position = (100, 200)
body.apply_impulse_at_local_point((100, 0), (0, 1))

shape = pymunk.Segment(body, (-50, 0), (50, 0), radius=10)
shape.elasticity = 0.999
space.add(body, shape)

App().run()