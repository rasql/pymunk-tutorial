from auto import *

img = """
.......
.xxx...
.xxx...
..xx...
..xxxx.
..xxxx.
.......
""".split()

segments = []

def segment_func(p0, p1):
    segments.append((p0, p1))

def sample_func(point):
    x = int(point.x)
    y = 6-int(point.y)
    return 1 if img[y][x] == 'x' else 0

bb = pymunk.BB(0, 0, 6, 6)
threshold = 0.5
march_soft(bb, 7, 7, threshold, segment_func, sample_func)

d = 30
for (a, b) in segments:
    segment = pymunk.Segment(space.static_body, d*a, d*b, 1)
    space.add(segment)

App().run()