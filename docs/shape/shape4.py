from shape import pymunk, space, App, Box, info

Box()

for i in range(10):
    body = pymunk.Body(mass=1, moment=1000)
    body.position = (100, 200)
    body.apply_impulse_at_local_point((100, 0), (0, 1))

    s1 = pymunk.Segment(body, (0, 0), (50, 0), 8)
    s1.density = 1
    s2 = pymunk.Segment(body, (0, 0), (0, 30), 8)
    s2.density = 1

    s1.elasticity = 0.999
    s2.elasticity = 0.999
    space.add(body, s1, s2)

info(body)
App().run()