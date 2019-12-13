# motors
from joint import pymunk, space, App, Box, Rectangle, Segment, Vec2d

Box()

b0 = space.static_body

p0 = 200, 120
arm = Segment(p0, (80, 10))
joint = pymunk.constraint.PivotJoint(b0, arm.body, p0)
space.add(joint)

p1 = 400, 120
arm = Segment(p1, (80, 10))
j1 = pymunk.constraint.PivotJoint(b0, arm.body, p1)
j2 = pymunk.constraint.SimpleMotor(b0, arm.body, 10)
space.add(j1, j2)

p2 = 600, 120
arm = Segment(p2, (80, 10))
j2 = pymunk.constraint.SimpleMotor(b0, arm.body, 10)
space.add(j2)

App().run()