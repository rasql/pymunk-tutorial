from intro import pymunk, space, App

b0 = space.static_body 

for i in range(5):
    body = pymunk.Body(mass=1, moment=10)
    body.position = (200+i*40, 50)
    if i==0:
        body.position = 50, 200
    shape = pymunk.Circle(body, radius=20)
    shape.elasticity = 0.999
    joint = pymunk.constraint.PinJoint(b0, body, (200+i*40, 200))
    space.add(body, shape, joint)

App().run()