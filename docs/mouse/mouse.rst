Using mouse and keyboard
========================

In this section we look at using the mouse and keyboard 
to interact with bodies.

Create balls at random locations
--------------------------------

We create a box and place 9 balls at random positions. 
In this example there is no gravity.::

    Box()

    r = 30
    for i in range(9):
        x = random.randint(r, w-r)
        y = random.randint(r, h-r)
        Circle((x, y), r)

.. image:: mouse1.png


Select a ball with the mouse
----------------------------

Now let's use the ``MOUSEBUTTONDOWN`` event to select an 
active shape with a mouse click::

    elif event.type == MOUSEBUTTONDOWN:
        p = from_pygame(event.pos, self.screen)
        self.active_shape = None
        for s in space.shapes:
            dist, info = s.point_query(p)
            if dist < 0: 
                self.active_shape = s

When there is an active shape, we surround it with a red circle::

    if self.active_shape != None:
        s = self.active_shape
        r = int(s.radius)
        p = to_pygame(s.body.position, self.screen)
        pygame.draw.circle(self.screen, RED, p, r, 3)

.. image:: mouse2.png


Move the active shape with keys
-------------------------------

Let's use the arrow keys to move the active object.
For this we define a dictionary where we association the 4 direction
unit vectors with the 4 arrow keys. If the key pressed is an arrow key,
we move the active shape 20 pixels into that direction::

    keys = {K_LEFT: (-1, 0), K_RIGHT: (1, 0),
            K_UP: (0, 1), K_DOWN: (0, -1)}
    if event.key in keys:
        v = Vec2d(keys[event.key]) * 20
        if self.active_shape != None:
            self.active_shape.body.position += v


Rotating an object with the mouse
---------------------------------

We can use the mouse-click into an object to change its angle.
All we need to add is this line of code in the ``MOUSEBUTTONDOWN`` section::

    s.body.angle = (p - s.body.position).angle

.. image:: mouse3.png


Pull a ball with the mouse
--------------------------

When releasing the mouse button, we take the mouse position and apply
an impulse to the ball which is proportional to the red line drawn with
the mouse, with ``p0`` being the object position and ``p1`` being 
the mouse position::

    elif event.type == MOUSEBUTTONUP:
        if self.pulling:
            self.pulling = False
            b = self.active_shape.body
            p0 = Vec2d(b.position)
            p1 = from_pygame(event.pos, self.screen)
            impulse = 100 * Vec2d(p0 - p1).rotated(-b.angle)
            b.apply_impulse_at_local_point(impulse)

To draw the red line we add this to the drawing code::

    if self.active_shape != None:
        b = self.active_shape.body
        r = int(self.active_shape.radius)
        p0 = to_pygame(b.position, self.screen)
        pygame.draw.circle(self.screen, RED, p0, r, 3)
        if self.pulling:
            pygame.draw.line(self.screen, RED, p0, self.p, 3)
            pygame.draw.circle(self.screen, RED, self.p, r, 3)

Which results in this

.. image:: mouse4.png

Source code
-----------

Here is the complete file.

:download:`mouse.py<mouse.py>`

.. literalinclude:: mouse.py

