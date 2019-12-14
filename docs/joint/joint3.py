# motors
from joint import b0, App, Box, PivotJoint, SimpleMotor, Segment, Vec2d

Box()

p0 = 200, 120
v = 80,10
arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)

p1 = 400, 120
arm = Segment(p1, v)
PivotJoint(b0, arm.body, p1)
SimpleMotor(b0, arm.body, 10)

p2 = 600, 120
arm = Segment(p2, v)
SimpleMotor(b0, arm.body, 10)

App().run()