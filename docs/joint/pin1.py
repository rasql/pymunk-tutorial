# two pendulum of different length
from joint import b0, App, Circle, Vec2d, PinJoint

p0 = Vec2d(300, 200)
v = Vec2d(80, 0)

c = Circle(p0+v)
PinJoint(b0, c.body, p0)

c = Circle(p0+2*v)
PinJoint(b0, c.body, p0)

App().run()