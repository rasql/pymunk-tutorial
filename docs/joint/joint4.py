# different rotation speeds
from joint import b0, App, SimpleMotor, PivotJoint , Segment, Vec2d

p0 = 200, 120
v = 80, 0
arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 1)

p0 = 400, 120
arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 5)

p0 = 600, 120
arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 10)

App().run()