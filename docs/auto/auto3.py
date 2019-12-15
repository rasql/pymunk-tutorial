from auto import *

img = pygame.image.load('pymunk_logo.png')
w, h = img.get_size()
bb = pymunk.BB(0, 0, w, h)

print(img)
print(bb)


def sample_func(point):
    return img.get_at(point).a

print(img.get_at((0, 0)).a)
print(img.get_at((100, 100)).a)

print(sample_func((0, 0)))
print(sample_func((100, 100)))

lines = pymunk.autogeometry.PolylineSet()

def segment_func(v0, v1):
    lines.collect_segment(v0, v1)

segment_func((0, 0), (100, 100))

march_soft(bb, 10, 10, 99, segment_func, sample_func)

print(len(lines))

App().run()