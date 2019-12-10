from shape import pymunk, space, App, Box

Box()
body = pymunk.Body(mass=1, moment=1000)
body.position = (100, 200)
body.apply_impulse_at_local_point((100, 0))

c1 = pymunk.Circle(body, radius=20, offset=(-20, 0))
c1.elasticity = 0.999

c2 = pymunk.Circle(body, radius=30, offset=(30, 0))
c2.elasticity = 0.999
c2.color = (255, 0, 0, 0)

space.add(body, c1, c2)
App().run()