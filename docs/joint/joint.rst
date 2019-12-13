Constraints and joints
======================

A constraint describes how two bodies interact with each other.
Constraints can be simple joints, which allow bodies to pivot around each other.

Double pendulum
---------------


.. image:: joint1.png

:download:`joint1.py<joint1.py>`


Rag doll
--------

In a rag doll, the different segments of the same body can 
cross, without creating collisions.

.. image:: joint2.png

:download:`joint2.py<joint2.py>`


Motors
------

The ``SimpleMotor`` class keeps the relative angular velocity constant.
In the following example code we have 3 constraints:

* a pivot joint makes a segment rotation around a point
* a pivot + motor joint, makes a rotation around a pivot point at a constant angular speed (10 radians/s)
* a motor joint, makes a freely moving segment follow the motor angle

.. image:: joint3.png

:download:`joint3.py<joint3.py>`



.. image:: joint4.png

:download:`joint4.py<joint4.py>`


A car
-----

.. image:: joint5.png

:download:`joint5.py<joint5.py>`