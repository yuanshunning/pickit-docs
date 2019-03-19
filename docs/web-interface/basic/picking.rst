Picking
=======

.. raw:: html

   <div>

Pick-it comes with a set of options that allows configuring how detected
objects should be picked by a robot. These options, that can be found in
the Picking tab of the Pick-it web interface, are grouped in the
following categories:

-  `Note on frames <#frames%22>`__
-  `Object ordering <#object_ordering%22>`__
-  `Pick strategy <#pick_strategy%22>`__
-  `Collision prevention <#collision_prevention%22>`__

This article explains how to use all settings to get the most out of
your application. You will learn how to align object frames for picking,
prevent collisions with a bin or other objects and choose the pick
order.

.. rubric:: Note on frames
   :name: frames

Before we start, let's first define three frame types in Pick-it that
we'll need throughout the article.

-  Reference frame: The reference frame defines the location of your
   work space in which to find objects. It usually has a Z axis (blue)
   that points up.
-  The object frame is the default frame that Pick-it associates to a
   shape. It indicates where a detected object is located and how it is
   oriented. It is chosen by the Pick-it detection algorithms and cannot
   be modified. This frame might not always be the best choice to use
   for picking, which is why the pick frame exists.
-  The pick frame is what gets sent to the robot. It defines how a robot
   can pick or grasp a detected object and is derived from the object
   frame by changing settings in the Picking tab of the web interface.

|image0|

.. rubric:: Object ordering
   :name: object_ordering

Under object ordering, the order in which objects will be picked when
more than one object is detected is defined. See following article to
have more detailed information about the different options, `Object
ordering <https://support.pickit3d.com/article/211-object-ordering>`__.

.. rubric:: Pick strategy
   :name: pick_strategy

Under Pick strategy, it is defined if and how the pick frames should be
aligned. This is often used to optimize cycle time or to prevent bin
collision. Following settings can be applied:

-  `Object to reference frame
   alignment <https://support.pickit3d.com/article/212-object-to-reference-frame-alignment>`__\ (Flex
   and Pattern only)
-  `Pick
   strategy <https://support.pickit3d.com/article/213-pick-strategy>`__\ (Flex:
   cylinders and spheres only)
-  `Enforce alignment of Pick frame
   orientation <https://support.pickit3d.com/article/214-enforce-alignment-of-pick-frame-orientation>`__

.. rubric:: Collision prevention
   :name: collision_prevention

This section explains how to prevent collisions when picking objects
with a robot. Objects that will not be picked because of collision
constraints will be labeled as unpickable and not sent to the robot. In
the Pick-it web interface, unpickable objects are displayed orange in
the Objects view and the `detection
grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__.

.. rubric:: Maximum angles
   :name: maximum-angles

To define objects as unpickable two overall angles can be defined. If
the calculated pick frame is bigger than either angle it is seen as
unpickable and will not be sent to the robot.

-  `Maximum angle between pick and reference frame
   Z-axes <https://support.pickit3d.com/article/215-maximum-angle-between-pick-and-reference-frame-z-axis>`__
-  `Maximum angle between pick frame Z-axis and surface normal(only if
   alignment is
   enforced) <https://support.pickit3d.com/article/216-maximum-angle-between-pick-frame-z-axis-and-surface-normal>`__

.. rubric:: Check collisions with
   :name: check-collisions-with

Pick-it also checks for possible collisions in the actual scene. For
this, first a `robot
tool  <https://support.pickit3d.com/article/217-robot-tool-model>`__\ needs
to be modeled. And second you have to define with what you want to check
collision with: bin and/or other objects. More detailed information on
how to use this feature can be found in this article, `check collision
with <https://support.pickit3d.com/article/218-check-collisions-with>`__.

.. raw:: html

   </div>

Mentioned articles

What to read next

| `Pick-it detection
  grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__

| `Region of
  Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
| `Detection: Pick-it
  Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
| `Detection:
  Pick-it Pattern <https://support.pickit3d.com/article/161-detection-pick-it-pattern>`__
| `Detection:
  Pick-it Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__

.. |image0| image:: https://lh3.googleusercontent.com/dBxTCKnpjv0hkRZSyIAHbTDp_6YQaFpnw-6dwml-t-rCCV-yD_KRG-ZKohoV4ukdOoWU8_DJcMVOjPjcdK87nzGnEirZSMwfx0otkzH7MwR5bFFLh-WuiKXE0RkucEH44Ap93cBW
   :width: 624px
   :height: 339px
