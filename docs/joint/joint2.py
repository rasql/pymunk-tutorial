# rag doll
from joint import pymunk, space, App, Box, Poly, PivotJoint, Segment, Vec2d

Box()

p0 = Vec2d(200, 150)
vs = [(-30, 50), (30, 50), (40, -50), (-40, -50)]
v0, v1, v2, v3 = vs
torso = Poly(p0, vs)
c = pymunk.Circle(torso.body, 20, (0, 70))
space.add(c)

v = Vec2d(60, 0)

arm = Segment(p0+v0, -v)
PivotJoint(torso.body, arm.body, v0, (0, 0))

forearm = Segment(p0+v0-v, -v)
PivotJoint(arm.body, forearm.body, -v, (0, 0))

arm = Segment(p0+v1, v)
PivotJoint(torso.body, arm.body, v1, (0, 0))

forearm = Segment(p0+v1+v, v)
PivotJoint(arm.body, forearm.body, v, (0, 0))

leg = Segment(p0+v2, (20, -100))
PivotJoint(torso.body, leg.body, v2, (0, 0))

leg = Segment(p0+v3, (-10, -100))
PivotJoint(torso.body, leg.body, v3, (0, 0))

App().run()