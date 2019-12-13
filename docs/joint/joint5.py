# car
from joint import pymunk, space, App, Box, Rectangle, Segment, Poly, Vec2d

Box()

p0 = Vec2d(200, 150)
vs = [(-50, -30), (50, -30), (50, 30), (-50, 30)]
chassis = Poly(p0, vs)

class Circle:
    def __init__(self, pos, radius=20):
        self.body = pymunk.Body()
        self.body.position = pos
        shape = pymunk.Circle(self.body, radius)
        shape.density = 0.1
        shape.elasticity = 0.5
        shape.friction = 0.9
        shape.color = (255, 0, 0, 0)
        shape.filter = pymunk.ShapeFilter(group=1)
        space.add(self.body, shape)


wheel1 = Circle(p0+vs[0])
wheel2 = Circle(p0+vs[1])

j1 = pymunk.constraint.PivotJoint(chassis.body, wheel1.body, vs[0], (0, 0))
j2 = pymunk.constraint.SimpleMotor(chassis.body, wheel1.body, 10)
space.add(j1, j2)

j1 = pymunk.constraint.PivotJoint(chassis.body, wheel2.body, vs[1], (0, 0))
j2 = pymunk.constraint.SimpleMotor(chassis.body, wheel2.body, 10)
space.add(j1, j2)

App().run()