# slide joint with colliding bodies True/False
from joint import App, Box, Circle, Segment, SimpleMotor, PivotJoint, Vec2d, b0, pymunk, space

Box()

p0 = Vec2d(200, 120)
v = Vec2d(80, 0)
r = 15
min, max = 30, 60

arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 1)

ball = Circle(p0+v+(40, 0), r)
SlideJoint(arm.body, ball.body, v, (-r, 0), min, max)

p0 += (200, 0)
arm = Segment(p0, v)
PivotJoint(b0, arm.body, p0)
SimpleMotor(b0, arm.body, 1)

ball = Circle(p0+v+(40, 0), r)
SlideJoint(arm.body, ball.body, v, (-r, 0), min, max, False)

App().run()