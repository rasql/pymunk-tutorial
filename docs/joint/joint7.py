# groove joint with collideing bodies False

from joint import b0, App, Box, Circle, GrooveJoint, Segment, SimpleMotor, PivotJoint, Vec2d

Box()

p0 = Vec2d(200, 120)
v = Vec2d(80, 0)
arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 1)

ball = Circle(p0+v, 20)
GrooveJoint(arm.body, ball.body, (0, 0), v, (0, 0))

p0 = Vec2d(400, 120)
arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 2)

ball = Circle(p0+v, 20)
GrooveJoint(arm.body, ball.body, (0, 0), 2*v, (0, 0))

App().run()