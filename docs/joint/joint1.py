# double pendulum
from joint import pymunk, space, App, Box, Rectangle

b0 = space.static_body
p0 = 100, 200

class Disc:
    def __init__(self, pos, radius=20):
        self.body = pymunk.Body(mass=1, moment=10)
        self.body.position = pos
        shape = pymunk.Circle(self.body, radius)
        space.add(self.body, shape)

p0 = 300, 200
d = Disc((120, 200), 30)
joint = pymunk.constraint.PinJoint(b0, d.body, p0)
space.add(joint)

p1 = 300, 200
d = Disc((200, 200), 30)
joint = pymunk.constraint.PinJoint(b0, d.body, p0)
space.add(joint)

App().run()