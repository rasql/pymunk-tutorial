from shape import pymunk, space, App, Box, info

Box()

for i in range(10):
    body = pymunk.Body(1, 100)
    body.position = (100+i*50, 150)
    body.apply_impulse_at_local_point((100, 0), (0, 10))
    
    shape = pymunk.Poly(body, [(0, 0), (60, 0), (30, 60)])
    shape.density = 0.1
    shape.elasticity = 1
    
    space.add(body, shape)

info(body)
App().run()