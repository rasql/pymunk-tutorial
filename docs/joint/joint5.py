# car with pivot and motor joint
from joint import App, Box, Circle, PivotJoint, SimpleMotor, Segment, Poly, Vec2d

Box()

p0 = Vec2d(200, 150)
vs = [(-50, -30), (50, -30), (50, 30), (-50, 30)]
v0, v1, v2, v3 = vs
chassis = Poly(p0, vs)

wheel1 = Circle(p0+v0)
wheel2 = Circle(p0+v1)

PivotJoint(chassis.body, wheel1.body, v0, (0, 0))
SimpleMotor(chassis.body, wheel1.body, 5)

PivotJoint(chassis.body, wheel2.body, v1, (0, 0))
SimpleMotor(chassis.body, wheel2.body, 5)

App().run()