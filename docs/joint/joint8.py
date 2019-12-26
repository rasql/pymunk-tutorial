# damped rotary spring
# limit rotary joint

from joint import b0, App, Segment, DampedRotarySpring, PivotJoint, RotaryLimitJoint, SimpleMotor, Vec2d

p0 = Vec2d(100, 110)
v = Vec2d(50, 0)

arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 1)

arm2 = Segment(p0+v, v)
PivotJoint(arm.body, arm2.body, v, (0, 0))
DampedRotarySpring(arm.body, arm2.body, 0, 10000000, 10000)

p0 = Vec2d(300, 110)
arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 1)

arm2 = Segment(p0+v, v)
PivotJoint(arm.body, arm2.body, v, (0, 0))
RotaryLimitJoint(arm.body, arm2.body, -1, 1)

App().run()