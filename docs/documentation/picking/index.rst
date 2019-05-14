.. _Picking:

Picking
=======

Pickit comes with a set of options that allows configuring how detected
objects should be picked by a robot. These options, that can be found in
the Picking tab of the Pickit web interface.

This article explains how to use all settings to get the most out of
your application. You will learn how to align object frames for picking,
prevent collisions with a bin or other objects and choose the pick
order.

Note on frames
--------------

Before we start, let's first define three frame types in Pickit that
we'll need throughout the article.

-  Reference frame: The reference frame defines the location of your
   work space in which to find objects. It usually has a Z axis (blue)
   that points up.
-  The object frame is the default frame that Pickit associates to a
   shape. It indicates where a detected object is located and how it is
   oriented. It is chosen by the Pickit detection algorithms and cannot
   be modified. This frame might not always be the best choice to use
   for picking, which is why the pick frame exists.
-  The pick frame is what gets sent to the robot. It defines how a robot
   can pick or grasp a detected object and is derived from the object
   frame by changing settings in the Picking tab of the web interface.

.. image:: /assets/images/Documentation/Note-on-frames.png

Object ordering
---------------

Under object ordering, the order in which objects will be picked when
more than one object is detected is defined. See following article to
have more detailed information about the different options.

.. toctree::
    :maxdepth: 1
    :glob:

    object-ordering

Pick strategy
-------------

Under Pick strategy, it is defined if and how the pick frames should be
aligned. This is often used to optimize cycle time or to prevent bin
collision. Following settings can be applied:

.. toctree::
    :maxdepth: 1
    :glob:

    object-to-reference-frame-alignment
    pick-strategy
    enforce-alignment-of-pick-frame-orientation

Collision prevention
--------------------

This section explains how to prevent collisions when picking objects
with a robot. Objects that will not be picked because of collision
constraints will be labeled as unpickable and not sent to the robot. In
the Pickit web interface, unpickable objects are displayed orange in
the Objects view and the :ref:`detection-grid`.

Maximum angles
~~~~~~~~~~~~~~

To define objects as unpickable two overall angles can be defined. If
the calculated pick frame is bigger than either angle it is seen as
unpickable and will not be sent to the robot.

.. toctree::
    :maxdepth: 1
    :glob:

    maximum-angle-between-pick-and-reference-frame-zaxis
    maximum-angle-between-pick-frame-zaxis-and-surface-normal

Check collisions with the robot tool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pickit also checks for possible collisions in the actual scene. For
this, first a robot tool needs to be modeled. And second you have to define with what you want to check
collision with: bin and/or other objects. More detailed information on
how to use this feature can be found in these articles.

.. toctree::
    :maxdepth: 1
    :glob:

    robot-tool-model
    check-collisions-with