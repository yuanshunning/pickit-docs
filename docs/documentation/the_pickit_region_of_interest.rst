The Pick-it Region of Interest
==============================

 1
    `What is the Region of Interest? <#roi_definition>`__
 2
    `Defining the Region of Interest <#define>`__
 3
    `Modifying the Region of Interest <#modify>`__
 4
    `Advanced Region of Interest filters <#advanced>`__

What is the Region of Interest?
-------------------------------

The **Region of Interest box (ROI box)** is the 3D region where object
detection takes place. 

In many applications, the field of view of the Pick-it camera is greater
than the region where we want to performing object detection. For
example, in a bin picking application we're only interested in the
contents of the bin. In the below image, we compare the camera field of
view ( **3D** tab of viewer), with the contents of the ROI box
(**Points** tab of viewer).

|image0|

By specifying a correct ROI box, we get **faster detection times**, as
Pick-it doesn't have to look for objects where they are not expected. In
the above example, object detection with the shown ROI box is between
two and three times faster than on the entire scene.

The ROI box can also be used to **prevent unwanted detections**, for
example if two bins are visible to the camera, but we only want to pick
objects from one. Setting the ROI box around one of the bins will ignore
the contents of the other.

For **bin picking** applications, the ROI box can be used for **bin
representation**, by fitting it to the internal borders of the bin.
Pick-it then can (optionally) perform bin collision avoidance and
prevention. Refer to the \ `How can I get a better bin picking
experience? <https://support.pickit3d.com/article/81-how-can-i-get-a-better-bin-picking-experience>`__
article for more information on how to make the best use of the ROI box
for such applications.

The ROI box can be defined and modified from the **Region of Interest**
page of the Pick-it web interface, and the points contained in it can be
visualized in the **Points** tab of the viewer.

Defining the Region of Interest
-------------------------------

There exist three methods in Pick-it for defining the ROI box:

#. `Use markers <#markers>`__
#. `Use plane <#plane>`__
#. `Use camera <#camera>`__

When a ROI box is defined, it also specifies the  **Pick-it reference
frame**. The axes of this frame are aligned with the box, and box bounds
are reported with respect to this frame, as mentioned in the \ `modify
the Region of Interest
section <https://support.pickit3d.com/article/42-define-the-boundaries-of-your-application-with-the-roi-box#modify>`__. Furthermore,
the position of the detected objects displayed in the \ `detection
grid <https://support.pickit3d.com/article/57-the-pick-it-detection-grid>`__
is with respect to the Pick-it reference frame.

Note that object positions are reported with respect to the **Pick-it
reference frame** in the web interface (`detection
grid <https://support.pickit3d.com/article/57-the-pick-it-detection-grid>`__)
for convenience; but they are sent to the robot with respect to the
**robot base frame**.

Use markers
~~~~~~~~~~~

This is the most common way of defining the ROI box. The ROI box is
defined based on three markers laid out in the field of view of the
camera. The Pick-it text of all markers should be oriented in the same
direction. The markers are not exchangeable, and can be identified by
the black alignment lines in the outer white border of each marker. The
'bottom-left' corner marker has two alignment lines that should point to
the corresponding 'top' and 'right' markers.

|image1|

#. Open the **Region of Interest** page on the Pick-it web interface
#. Place the three markers as shown in the image below in the field of
   view of the camera
#. Press Use markers (this button is on clickable when all three markers
   are in the field of view of the camera)
#. If required, manually adjust the ROI box size as described in
   the \ `modify the Region of Interest
   section <https://support.pickit3d.com/article/42-define-the-boundaries-of-your-application-with-the-roi-box#modify>`__.

Note that simultaneously with defining the ROI box the **Pick-it
reference frame** is defined in the left bottom corner of the ROI box.

|image2|

Use plane
~~~~~~~~~

With this strategy, the ROI box is located on top of the most dominant
plane in the field of view of the camera.

#. Open the **Region of Interest** page on the Pick-it web interface
#. Press Use plane
#. Input length and width of the desired ROI box
#. If required, manually adjust the ROI box size as described in
   the \ `modify the Region of Interest
   section <https://support.pickit3d.com/article/42-define-the-boundaries-of-your-application-with-the-roi-box#modify>`__.

Note that simultaneously with defining the ROI box the **Pick-it
reference frame** is defined in the middle of the bottom of the ROI box.

Use camera
~~~~~~~~~~

In this way the ROI box is defined based of the camera frame.

#. Open the **Region of Interest** page on the Pick-it web interface
#. Press Use camera
#. Input length and width of the desired ROI box
#. If required, manually adjust the ROI box size as described in
   the \ `modify the Region of Interest
   section <https://support.pickit3d.com/article/42-define-the-boundaries-of-your-application-with-the-roi-box#modify>`__.

Note that this method simply defines the camera frame as the **Pick-it
reference frame**.

Modifying the Region of Interest
--------------------------------

Once an initial ROI box has been defined, you can manually adjust its
size and position, but not its orientation. When the **Region of
Interest** page is open, colored arrows attached to the ROI are
displayed in the viewer (in all views except 2D). Arrows are colored
according to the Pick-it reference frame direction: X→red, Y→green,
Z→blue. You can interactively click and drag the arrows to extend and
contract the box along each of its sides.

|image3|

The exact bounds and size of the ROI box are reported in the  **Region
of Interest** page, as shown below. You can also manually set the bound
values here and the ROI box will be updated in the viewer.

|image4|

Example 1: Modify ROI box to remove the ground plane
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Removing the ground plane from the ROI box is one of the simplest ways
to have faster detection times. The below sequence shows the **Points**
view before and after raising the bottom of the box just above the
ground plane.

|image5|

Example 2: Bin representation with the ROI box
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To use the ROI box as an approximate representation of the bin, we
recommend to define it  `using markers <#markers>`__, and aligning them
with the bin corners. Once the initial ROI box is set with a correct
orientation, adjust the borders such that it excludes most bin points,
and includes all relevant bin contents. The below sequence shows
the \ **Points** view before and after adjusting the box boundaries to
the inside of the bin.

|image6|

Attaching the Region of Interest to the world
---------------------------------------------

Now that you know how to define and modify a ROI box, you need to decide
where it is attached to. The ROI box can be attached to either the
**camera** or the \ **robot base**. This distinction is meaningful for
robot-mounted camera scenarios:

Camera
^^^^^^

A ROI box attached to the  **camera** moves relative to the robot base
as the robot end-effector (and camera) move.To define the ROI box,
a running connection between Pick-it and the robot is **not required**.

|image7|

Robot base
^^^^^^^^^^

| A ROI box attached to the  **robot base** remains stationary relative
  to the robot base as the robot end-effector (and camera) move. 
| This is the recommended attachment for camera-on-robot scenarios. To
  define the ROI box, a running connection between Pick-it and the robot
  is  **required**.

Refer to the  `Attach the ROI Box to the robot base for picking objects
from a big
bin <https://support.pickit3d.com/article/41-attaching-the-roi-box-to-the-robot-base-for-binpicking-objects-from-a-big-bin>`__
article for an example application

|image8|
^^^^^^^^

Advanced Region of Interest filters
-----------------------------------

There are a number of advanced Region of Interest filters used for
excluding points **inside** **the ROI box.** These are explained in
the \ `How to use the color
filter <https://support.pickit3d.com/article/63-how-to-use-the-color-filter>`__
and  \ `Advanced Region of Interest
filters <https://support.pickit3d.com/article/90-advanced-roi-filters>`__
articles.

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb66b22c7d3a0e93671fdc/file-ormnI6ZCCv.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58fdf1c80428634b4a328b69/file-3m1oc8lGI2.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58fe1a1f2c7d3a057f887f26/file-KwOsSJURle.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb5c4104286307509234ea/file-XknBCpZ4Qk.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb38272c7d3a0e93671e4b/file-tFzSOxKm4i.png
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb5eaa2c7d3a0e93671f90/file-WVA1L2jEyk.png
.. |image6| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb73b82c7d3a0e93672068/file-L0udK6oyqp.png
.. |image7| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acc797704286307509242b1/file-zF0gwfhJ0N.png
.. |image8| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acc79492c7d3a0e93672c9f/file-z7XTnEif5D.png

