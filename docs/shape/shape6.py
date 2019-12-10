from shape import pymunk, space, App, Box, Polygon

Box()

vertices = [(0, 0), (60, 0), (30, 60)]
for i in range(10):
    Polygon((100+i*50, 150), vertices)

App().run()