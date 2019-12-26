# gear joint
from joint import *

p0 = Vec2d(100, 100)
r1, r2 = 40, 80
v = Vec2d(r1+r2, 0)
wheel1 = Circle(p0, r1)
wheel2 = Circle(p0+v, r2)

SimpleMotor(b0, wheel1.body, 5)
PivotJoint(b0, wheel1.body, p0)
PivotJoint(b0, wheel2.body, p0+v)
GearJoint(wheel1.body, wheel2.body, 0, -r2/r1)

App().run()