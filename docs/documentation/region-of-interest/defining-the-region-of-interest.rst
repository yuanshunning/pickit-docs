Defining the Region of Interest
-------------------------------

There are three methods in Pickit for defining the ROI box:

-  `Use markers <#markers>`__
-  `Use plane <#plane>`__
-  `Use camera <#camera>`__

When a ROI box is defined, it specifies the **Pickit reference frame**.
The axes of this frame are aligned with the box, and box bounds are
reported with respect to this frame, as mentioned in the \ `modifying
the Region of Interest section <#modifying>`__. Furthermore, the
position of the detected objects displayed in the \ `detection
grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__
is with respect to the Pickit reference frame.

Note that object positions are reported with respect to the Pickit
reference frame in the web interface (`detection
grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__)
for convenience; but they are sent to the robot with respect to
the robot base frame.

Use markers
~~~~~~~~~~~

This is the most common way of defining the ROI box. The ROI box is
defined based on three markers laid out in the field of view of the
camera. The Pickit text of all markers should be oriented in the same
direction. The markers are not exchangeable, and can be identified by
the black alignment lines in the outer white border of each marker. The
'bottom-left' corner marker has two alignment lines that should point to
the corresponding 'top' and 'right' markers.

|image1|

#. Open the \ **Region of Interest** page on the Pickit web interface.
#. Place the three markers as shown in the image below in the field of
   view of the camera.
#. Press Use markers (this button is on clickable when all three markers
   are in the field of view of the camera).
#. If required, manually adjust the ROI box size as described in
   the \ `modifying the Region of Interest section <#modifying>`__.

Note that when defining the ROI box, the \ **Pickit reference
frame** is defined in the left bottom corner of the ROI box.

|image2|

Use plane
~~~~~~~~~

With this strategy, the ROI box is located on top of the most dominant
plane in the field of view of the camera.

#. Open the \ **Region of Interest** page on the Pickit web interface.
#. Press Use plane.
#. Input length and width of the desired ROI box.
#. If required, manually adjust the ROI box size as described in
   the \ `modifying the Region of Interest section <#modifying>`__.

Note that when defining the ROI box, the \ **Pickit reference
frame** is defined in the middle of the bottom of the ROI box.

Use camera
~~~~~~~~~~

In this way the ROI box is defined based of the camera frame.

#. Open the Region of Interest page on the Pickit web interface.
#. Press Use camera.
#. Input length and width of the desired ROI box.
#. If required, manually adjust the ROI box size as described in
   the \ `modifying the Region of Interest section <#modifying>`__.

Note that this method simply defines the camera frame as the \ **Pickit
reference frame**.

.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58fdf1c80428634b4a328b69/file-3m1oc8lGI2.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/58fe1a1f2c7d3a057f887f26/file-KwOsSJURle.png