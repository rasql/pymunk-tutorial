# different rotation speeds
from joint import pymunk, space, App, Box, Rectangle, Segment, Vec2d

Box()

b0 = space.static_body

p0 = 200, 120
arm = Segment(p0, (80, 10))
j1 = pymunk.constraint.PivotJoint(b0, arm.body, p0)
j2 = pymunk.constraint.SimpleMotor(b0, arm.body, 1)
space.add(j1, j2)

p0 = 400, 120
arm = Segment(p0, (80, 10))
j1 = pymunk.constraint.PivotJoint(b0, arm.body, p0)
j2 = pymunk.constraint.SimpleMotor(b0, arm.body, 10)
space.add(j1, j2)

p0 = 600, 120
arm = Segment(p0, (80, 10))
j1 = pymunk.constraint.PivotJoint(b0, arm.body, p0)
j2 = pymunk.constraint.SimpleMotor(b0, arm.body, 20)
space.add(j1, j2)

App().run()