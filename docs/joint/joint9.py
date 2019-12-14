# rachet joint

from joint import pymunk, space, App, Box, Segment, PivotJoint, RatchetJoint, SimpleMotor, Vec2d
import math

b0 = space.static_body

p0 = Vec2d(200, 120)
v = Vec2d(80, 0)
arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 1)

arm2 = Segment(p0+v, v)
PivotJoint(arm.body, arm2.body, v)
RatchetJoint(arm.body, arm2.body, 0, math.pi/2)

p0 = Vec2d(400, 120)
arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 1)

arm2 = Segment(p0+v, v)
PivotJoint(arm.body, arm2.body, v)
RatchetJoint(arm.body, arm2.body, 0, math.pi/8)

App().run()