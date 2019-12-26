# motors
from joint import *
Box()

p = 100, 120
v = 60,10
arm = Segment(p, v)
PivotJoint(b0, arm.body, p)

p1 = 200, 120
arm = Segment(p1, v)
PivotJoint(b0, arm.body, p1)
SimpleMotor(b0, arm.body, 10)

p2 = 300, 120
arm = Segment(p2, v)
SimpleMotor(b0, arm.body, 10)

App().run()