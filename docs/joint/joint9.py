# rachet joint
from joint import *

p0 = Vec2d(100, 120)
v = Vec2d(60, 0)
arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 1)

arm2 = Segment(p0+v, v)
PivotJoint(arm.body, arm2.body, v)
RatchetJoint(arm.body, arm2.body, 0, math.pi/2)

p0 = Vec2d(300, 120)
arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 1)

arm2 = Segment(p0+v, v)
PivotJoint(arm.body, arm2.body, v)
RatchetJoint(arm.body, arm2.body, 0, math.pi/8)

App().run()