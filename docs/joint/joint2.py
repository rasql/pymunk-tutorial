#rag doll
from joint import pymunk, space, App, Box, Rectangle, Segment, Poly, Vec2d

Box()

p0 = Vec2d(200, 150)
vs = [(-30, 50), (30, 50), (40, -50), (-40, -50)]
torso = Poly(p0, vs)

arm = Segment(p0+vs[0], (-60, 10))
joint = pymunk.constraint.PivotJoint(torso.body, arm.body, (-30, 50), (0, 0))
space.add(joint)

arm2 = Segment(p0+vs[1], (60, 10))
joint = pymunk.constraint.PivotJoint(torso.body, arm2.body, (30, 50), (0, 0))
space.add(joint)

forarm = Segment((290, 200), (60, 10))
joint = pymunk.constraint.PivotJoint(arm2.body, forarm.body, (60, 10), (0, 0))
space.add(joint)

forarm = Segment((110, 200), (-60, -10))
joint = pymunk.constraint.PivotJoint(arm.body, forarm.body, (-60, 10), (0, 0))
space.add(joint)

leg = Segment(p0+vs[2], (10, -100))
joint = pymunk.constraint.PivotJoint(torso.body, leg.body, (30, -50), (0, 0))
space.add(joint)

leg2 = Segment(p0+vs[3], (-10, -100))
joint = pymunk.constraint.PivotJoint(torso.body, leg2.body, (-30, -50), (0, 0))
space.add(joint)

App().run()