# double pendulum
from joint import *

p = Vec2d(200, 190 )
v = Vec2d(80, 0)

c = Circle(p+v)
PinJoint(b0, c.body, p)

c2 = Circle(p+2*v)
PinJoint(c.body, c2.body)

App().run()