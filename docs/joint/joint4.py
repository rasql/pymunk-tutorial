# different rotation speeds
from joint import *

p = 100, 100
v = 80, 0
arm = Segment(p, v)
PivotJoint(b0, arm.body, p)
SimpleMotor(b0, arm.body, 1)

p = 200, 100
arm = Segment(p, v)
PivotJoint(b0, arm.body, p)
SimpleMotor(b0, arm.body, 5)

p = 300, 100
arm = Segment(p, v)
PivotJoint(b0, arm.body, p)
SimpleMotor(b0, arm.body, 10)

App().run()