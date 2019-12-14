# pivot point
from joint import b0, App, PivotJoint, Segment, Vec2d

p0 = Vec2d(100, 200)
v = Vec2d(80, 0)

segment = Segment(p0, v)
PivotJoint(b0, segment.body, p0)

segment = Segment(p0+4*v, 2*v)
PivotJoint(b0, segment.body, p0+4*v)

segment2 = Segment(p0+6*v, v)
PivotJoint(segment.body, segment2.body, 2*v)

App().run()