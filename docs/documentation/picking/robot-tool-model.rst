Robot tool model
================

If a **collision checkbox** is checked, the robot tool model settings
are visible. These settings allow you to model your robot tool.

Why is it important to model your robot tool?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In picking applications, it is important to prevent that the robot
collides with the bin or potential other objects such that the
application can run without interruption. Starting from Pickit version
1.10, it is possible to model the robot tool to closely resemble the
actual tool that is mounted on the robot.

By modeling the robot tool more accurately, one can avoid that:

-  Objects are labeled unpickable although they could be picked without
   collision (tool modeled too conservative with respect to the actual
   robot tool).
-  Objects are labeled pickable although the robot will collide when
   picking them (tool model dimensions are smaller than actual robot
   tool models’).

Provided robot tool models
^^^^^^^^^^^^^^^^^^^^^^^^^^

The provided robot tool models are:

-  Two-finger gripper
-  Box-shaped tool
-  Cylinder-shaped tool

.. raw:: html

   <div class="callout-yellow">

**Note** The tool modelling view is hidden when collision checks are
disabled (Neither “Bin” or “Other objects” are selected).

.. raw:: html

   </div>

The screenshots below show an example of robot tool modelling for the
**box-shaped tool**.

|image0|

Every tool model can be customized to closely resemble the actual robot
tool. Besides the tool dimensions, one can also adapt distance and
orientation of the tool wrt. the object’s pick frame. However, be aware
that this doesn’t influence how the robot picks an object. These values
are only used for collision checking and have no effect on an object’s
pick frame.

.. |image0| image:: https://lh4.googleusercontent.com/LjpVJBQ1jROEFQJjRZM97cGHZaKcGwluzEw12ofofJzA4LzSxJu8ZovBzI0ITKOEfgG9xrlfCcFDkrFd1roMsoodGMdV5dsdVY3vjrstIUu8qIyMsCtJJfobSCexo20Zl7Ak60DN
   :width: 624px
   :height: 411px
