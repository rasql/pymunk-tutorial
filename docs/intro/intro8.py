from intro import pymunk, space, App

b0 = space.static_body 

b1 = pymunk.Body(mass=1, moment=10)
b1.position = (100, 200)
c1 = pymunk.Circle(b1, radius=20)
c1.elasticity = 0.999
space.add(b1, c1)

b2 = pymunk.Body(mass=1, moment=10)
b2.position = (240, 100)
c2 = pymunk.Circle(b2, radius=20)
c2.elasticity = 0.999
space.add(b2, c2)

j1 = pymunk.constraint.PinJoint(b0, b1, (200, 200))
j2 = pymunk.constraint.PinJoint(b0, b2, (240, 200))
space.add(j1, j2)

App().run()