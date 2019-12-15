Create an app
=============

In this section we are looking how to make an interactive application 
using Pymunk.

.. literalinclude:: app.py
   :pyobject: App


Circle
------

The ``Circle`` class creates a body with an attached circle shape.

.. literalinclude:: app.py
   :pyobject: Circle

This is an exemple of three circles placed in a no-gravity space::

    p0 = Vec2d(200, 120)
    v = Vec2d(100, 0)

    Space('Cercle', GRAY, gravity=(0, 0))
    Circle(p0)
    Circle(p0+v, 20)
    Circle(p0+2*v, 50, RED)

.. image:: app1.png

:download:`app.py<app.py>`


Segment
-------

The ``Segment`` class creates a linear segment starting at position ``p0``
having a direction vector ``v``, a radius and a color.

.. literalinclude:: app.py
   :pyobject: Segment

This is an example of two segments of different radius, length and color::

    Space('Segment', gravity=(0, 0))
    Segment(p0, v)
    Segment(p0+(50, 50), 2*v, 5, RED)

.. image:: app2.png


Poly
----

The ``Poly`` class creates a filled polygon placed at position ``p0`` 
with the vertices ``v`` given with a vertex list.

.. literalinclude:: app.py
   :pyobject: Poly

This is an example of creating a triangle and a square polygon::

    Space('Poly', gravity=(0, 0))
    triangle = [(-30, -30), (30, -30), (0, 30)]
    Poly(p0, triangle)
    square = [(-30, -30), (30, -30), (30, 30), (-30, 30)]
    Poly(p0+v, square)

.. image:: app3.png

