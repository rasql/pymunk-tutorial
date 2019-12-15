Auto-geometry
=============

The ``autogeometry`` module contains functions for automatic generation of
geometry. This can be used to create a segment line or a polygon.

Lets give an example with a 7x7 pixel image::

    img = """
    .......
    .xxx...
    .xxx...
    ..xx...
    ..xxxx.
    ..xxxx.
    .......
    """.split()

Which produces this list::

    ['.......', '.xxx...', '.xxx...', '..xx...', '..xxxx.', '..xxxx.', '.......']

Then we prepare an empty segment list 
and define two functions needed for the segmentation algorithm::

    segments = []

    def segment_func(p0, p1):
        segments.append((p0, p1))

    def sample_func(point):
        x = int(point.x)
        y = 6-int(point.y)
        return 1 if img[y][x] == 'x' else 0

Now we can call the ``march_hard`` segmentation algorithm::

    bb = pymunk.BB(0, 0, 6, 6)
    threshold = 0.5
    march_hard(bb, 7, 7, threshold, segment_func, sample_func)

The segment list can now be displayed either as segments or as polygon::

    d = 30
    for (a, b) in segments:
        segment = pymunk.Segment(space.static_body, d*a, d*b, 1)
        space.add(segment)

.. image:: auto1.png

:download:`auto1.py<auto1.py>`
:download:`auto.py<auto.py>`

Soft contour
------------

We can also trace an anti-aliased contour of an image 
by using the ``march_soft`` segmentation algorithm.

.. image:: auto2.png