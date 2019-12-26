# rag doll
from joint import *

Box()

p = Vec2d(200, 120)
vs = [(-30, 40), (30, 40), (40, -40), (-40, -40)]
v0, v1, v2, v3 = vs
torso = Poly(p, vs)

c = pymunk.Circle(torso.body, 20, (0, 60))
space.add(c)

v = Vec2d(60, 0)
arm = Segment(p+v0, -v)
PivotJoint(torso.body, arm.body, v0, (0, 0))

forearm = Segment(p+v0-v, -v)
PivotJoint(arm.body, forearm.body, -v, (0, 0))

arm = Segment(p+v1, v)
PivotJoint(torso.body, arm.body, v1, (0, 0))

forearm = Segment(p+v1+v, v)
PivotJoint(arm.body, forearm.body, v, (0, 0))

leg = Segment(p+v2, (20, -100))
PivotJoint(torso.body, leg.body, v2, (0, 0))

leg = Segment(p+v3, (-10, -100))
PivotJoint(torso.body, leg.body, v3, (0, 0))

App().run()