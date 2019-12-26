# slide joint with colliding bodies True/False
from joint import *

Box()

p = Vec2d(100, 120)
v = Vec2d(70, 0)
r = 15
min, max = 30, 60

arm = Segment(p, v)
PivotJoint(b0, arm.body, p)
SimpleMotor(b0, arm.body, 1)

ball = Circle(p+v+(40, 0), r)
SlideJoint(arm.body, ball.body, v, (-r, 0), min, max)

p2 = p + (150, 0)
arm = Segment(p2, v)
PivotJoint(b0, arm.body, p2)
SimpleMotor(b0, arm.body, 1)

ball = Circle(p2+v+(40, 0), r)
SlideJoint(arm.body, ball.body, v, (-r, 0), min, max, False)

App().run()