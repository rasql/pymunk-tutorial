from intro import pymunk, space, App

b0 = space.static_body 

body = pymunk.Body(mass=1, moment=10)
body.position = (100, 100)
circle = pymunk.Circle(body, radius=20)

joint = pymunk.constraint.PinJoint(b0, body, (200, 200))
space.add(body, circle, joint)

App().run()