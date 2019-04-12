Picking strategies
==================

Pickit comes with a set of options that allows configuring how detected
objects should be picked by a robot. These options, that can be found in
the  **Picking** tab of the Pickit web interface, are grouped in the
following categories:

-  `Pick strategy <#pick_strategy>`__
-  `Collision prevention <#collision_prevention>`__
-  `Object ordering <#object_ordering>`__

This article explains how to use all settings to get the most out of
your application. You will learn how to align object frames for picking,
prevent collisions with a bin or other objects and choose the pick
order.

Note on frames
--------------

Before we start, let's first define three frame types in Pickit that
we'll need throughout the article.

-  **Reference frame:** The reference frame defines the location of your
   workspace in which to find objects. It usually has a Z axis (blue)
   that points up.
-  The **object frame** is the default frame that Pickit associates to
   a shape. It indicates where a detected object is located and how it
   is oriented. It is chosen by the Pickit detection algorithms and
   cannot be modified. This frame might not always be the best choice to
   use for picking, which is why the pick frame exists.
-  The **pick frame** is what gets sent to the robot. It defines how a
   robot can pick or grasp a detected object and is derived from the
   object frame by changing settings in the Picking tab of the web
   interface.

|image0|

Pick strategy
-------------

Object to reference frame alignment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting aligns an object frame axis with a reference frame axis.
The newly created aligned frame is the pick frame that will be sent to
the robot. The setting smartly makes use of the symmetry of an object to
decide if object axes can be flipped so they point to the same direction
as the selected reference frame axes.

.. raw:: html

   <div class="callout-yellow">

**Note** This setting is only available with the **Flex** and **Teach
engine**.

.. raw:: html

   </div>

Two options need to be provided to make this work:

-  The **axis of the object frame** to align. The provided options are X
   or Y.
-  And the **axis of the reference frame** to align the object axis
   with. The provided options are X, -X, Y, -Y, Z or -Z.

The pictures below show examples of the object to reference frame
alignment setting for rectangular and circular shapes respectively:

|image1|

Pick strategy
~~~~~~~~~~~~~

.. raw:: html

   <div class="callout-yellow">

**Note** This setting is only available for **cylinder** and **sphere**
detections with the **Flex engine**.

.. raw:: html

   </div>

This setting allows you to move the pick frame to the real surface of
the detected object instead of the center of the object. The possible
options are:

-  **Default:** The default object frame will be used, which is a frame
   in the center of the cylinder or sphere. This option does not modify
   the pick frame.
-  **Surface top:** The pick frame will move to the center at the top
   surface of the object.
-  **Surface visible:** The pick frame will move to the center of the
   visible part of the object. This setting is useful to avoid
   collisions when the detected object is partially covered by another
   object.
-  **End circle:** The pick frame will be moved to the highest circular
   end of the cylinder.

.. raw:: html

   <div class="callout-yellow">

**Note** The resulting pick frame axes will not necessarily be parallel
to one of the reference frame axes. If you want this, use the **Enforce
alignment of pick frame orientation** option.

.. raw:: html

   </div>

The picture below shows an example of a spherical and cylindrical object
respectively:

|image2|

Enforce alignment of Pick frame orientation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This setting can be used to enforce aligning an object frame with the
reference frame. The newly created aligned frame is the pick frame that
will be sent to the robot. This setting will make sure that one or more
resulting pick frame axes have a parallel or perpendicular axis to the
reference frame axes.

.. raw:: html

   <div class="callout-red">

**Warning** Enforcing a pick frame orientation takes precedence over the
object to reference frame alignment.

.. raw:: html

   </div>

There are multiple alignment options:

-  **No alignment:** No alignment will be done, this option does not
   modify the pick frame.
-  **Y ⊥ Z:** Aligns the Y-axis of the pick frame to be in the XY plane
   of the reference frame.
-  **Z \|\| Z:** Aligns the Z-axis of the pick frame to be parallel to
   the Z axis of the reference frame. In most applications, the Z axis
   points up from the table or bin, so this option enforces the pick
   frame to point upwards.
-  **XYZ \|\| XYZ:** Aligns all three axis of the pick frame with all
   three axis of the reference frame.

When any of the alignment options is selected (except for 'No
alignment'), the following additional options appear. It is recommended
to leave these options to their default values or contact a support
engineer to set them.

-  **Distance from box for avoidance:** Default value 30 mm.
-  **Angular modification away from box:** Default value 20 degrees.
-  **Allowed correction axis deviation:** Default value 20 degrees.
-  **Allowed correction along pick frame Y axis:** Default value 20
   degrees.
-  **Avoid ROI sides treating object as:** Default value Preserve type.

The picture below shows an example of a bin with cylinders:

|image3|

Collision prevention
--------------------

This section explains how to prevent collisions when picking objects
with a robot. Objects that will not be picked because of collision
constraints will be labeled as unpickable and not sent to the robot. In
the Pickit web interface, unpickable objects are displayed orange in
the Objects view and the  `detection
grid <https://support.pickit3d.com/article/57-the-pick-it-detection-grid>`__.

Maximum angle between pick and reference frame Z-axis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With this setting, you can specify the maximum angular difference
between the Z axis of your pick frame and the Z axis of your reference
frame. If an object is tilted more than the maximum specified angle, the
object will be labeled as unpickable and not sent to the robot. In the
Pickit web interface, unpickable objects are displayed orange in the
Objects view and the  `detection
grid <https://support.pickit3d.com/article/57-the-pick-it-detection-grid>`__.

Check collisions with
~~~~~~~~~~~~~~~~~~~~~

This setting specifies for which obstacles collisions need to be
checked. The options are:

-  **Bin:** Prevents collisions between robot tool and region of
   interest. Typically the region of interest box boundaries corresponds
   to the boundaries of a bin in a bin-picking scenario.

   .. raw:: html

      <div class="callout-yellow">

   **Note** Bin avoidance constraints take precedence over other
   specified pick frame alignment constraints.

   .. raw:: html

      </div>

-  **Other objects:** Prevents collisions between the robot tool model
   and objects different from the one to pick.
-  **Robot motions:** Prevents collisions with the robot arm while it is
   moving towards an object. Imagine when a pile of things is standing
   in the way of the actual object that you want to pick, you don't want
   to make this pile collapse.

   -  **Position of collision-free volume:** Specifies on which side of
      the region of interest box, the robot is standing.
   -  **Length scaling factor (%) of collision-free volume:** Specifies
      the size of the volume around the object where the system doesn't
      check for other objects that are standing in the way.
   -  **Height of collision-free volume above reference frame:**
      Specifies the minimum height of the pile of objects for which the
      system needs to check collisions.

Robot tool model
~~~~~~~~~~~~~~~~

If the **bin collision checkbox** is checked, the robot tool model
settings are visible. These settings allow you to model your robot tool.

Why is it important to model your robot tool?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In bin picking applications, it is important to prevent that the robot
collides with the bin or potential other objects such that the
application can run without interruption. Starting from Pickit version
1.10, it is now possible to more accurately model the robot tool to
closely resemble the actual tool that is mounted on the robot.

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

**Note** that the tool modelling view is hidden when collision checks
are disabled (Neither “Bin” or “Other objects” are selected).

.. raw:: html

   </div>

The screenshots below show an example of robot tool modelling for the
**box-shaped tool**.

|image4|

Every tool model can be customized to closely resemble the actual robot
tool. Besides the tool dimensions, one can also adapt distance and
orientation of the tool wrt. the object’s pick frame. However, be aware
that this doesn’t influence how the robot picks an object. These values
are only used for collision checking and have no effect on an object’s
pick frame.

|image5|

When collision checking yields that a certain object pose will result in
a collision, the object status is rendered as unpickable which can be
seen in the objects table.

|image6|

When clicking on the unpickable object, the modeled tool will appear in
the “Objects” tab of the 3D view to illustrate why the given object is
unpickable. In the following example the object is labeled as unpickable
as the robot tool would collide with the bin borders in case the robot
would pick it.

|image7|

Object ordering
---------------

Under object ordering, you can define in which order objects will be
picked when more than one object is detected. Options are:

-  **Highest product center:** Sort objects with highest product center
   first. This is the most common option.
-  **Lowest product center:** Reverse ordering from 'Highest product
   center'.
-  **Highest product part:** Sort objects with highest volume or surface
   boundary first.
-  **Lowest X value first:** Orders objects based on object center
   position. From small to large X value.
-  **Highest X value first:** Reverse ordering from 'Lowest X value
   first'.
-  **Lowest Y value first:** Orders objects based on object center
   position. From small to large Y value.
-  **Highest Y value first:** Reverse ordering from 'Lowest Y value
   first'.
-  **Biggest product:** Objects are ordered from big to small volume or
   surface.
-  **Pattern along the positive X-axis:** See image below.
-  **Pattern along the negative X-axis:** See image below.
-  **Pattern along the positive Y-axis:** See image below.
-  **Pattern along the negative Y-axis:** See image below.
-  **Highest matching score (Teach only):** Sort objects with the
   highest model matching score first. This only works for the Teach
   detection

The pattern sort options are useful for depalletization or pallet
loading applications. The picture below illustrates each option:

|image8|

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5abdf8b1042863794fbec1ac/file-66mLZ7pD5u.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ac4f2df2c7d3a0e936702d1/file-YSiaSfA2dA.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ac4f06c2c7d3a0e936702bf/file-AIyAGwz6XG.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5abe4d19042863794fbec35b/file-yDidTrHTbG.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5c0500672c7d3a31944ea3d4/file-LyIs2v90bX.png
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5c05008604286304a71ce95c/file-35YUk3p2p4.png
.. |image6| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5c0500962c7d3a31944ea3d9/file-CsQIaEtsj7.png
.. |image7| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5c0500ab04286304a71ce95e/file-XX3Ab9jMWy.png
.. |image8| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5ac4f3592c7d3a0e936702d9/file-GQShjfESmv.png

