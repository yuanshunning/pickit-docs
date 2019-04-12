Viewer
======

The Pickit viewer is the main component of the Pickit web interface
for providing visual feedback on the camera view and detection results.
Textual and quantitative information from the detection results is
provided by the complementary  `Pickit detection
grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__
component.

The Pickit viewer consists of a number of 2D and 3D views arranged in
tabs:

-  `2D view <#2d>`__
-  `3D view <#3d>`__
-  `Points view <#points>`__
-  `Clusters view <#clusters>`__
-  `Objects view <#objects>`__
-  `Model view <#model>`__

The following overlays are shown in all views:

-  Top-left: Camera ID and indicator that a correct camera calibration
   was loaded.
-  Lower-left: \ `Save
   snapshot <https://support.pickit3d.com/article/168-saving-a-snapshot-in-pick-it>`__
   button and reset 3D view button (shown on mouse hover, not available
   in 2D view).
-  Lower right: Maximize/minimize button and View settings for
   customizing a particular view (shown on mouse hover).

|image0|

Also common to all views, a notification is displayed when no camera is
connected and no snapshot is loaded:

|image1|

2D view
~~~~~~~

Live 2D camera image stream when a camera is connected. It always
overlays on top of the image:

-  The Region of Interest box.
-  The Pickit Reference frame.

After each detection, object frames, picking order identifiers and
contour are also shown for a brief period of time.

|image2|

3D view
~~~~~~~

Live 3D camera image stream when a camera is connected. It also renders:

-  The Region of Interest box.
-  The Pickit Reference, robot base and robot end-effector frames.
-  Optionally: The Pickit camera(s) and robot (Universal Robots only)
   3D models.

|image3|

Points view
-----------

Displays the 3D point cloud used in the last Pickit detection. Only
points contained in the ROI box are shown. It also renders the same
additional elements listed for the the 3D view.

|image4|

Clusters view
~~~~~~~~~~~~~

Displays the 3D point clouds of all clusters found in the last Pickit
detection. Each cluster is shown in a different color. It also renders
the same additional elements listed for the the 3D view.

This view is only available for the Pickit Flex and Pattern detection
engines.

|image5|

Objects view
~~~~~~~~~~~~

Displays the 3D point clouds of all objects found in the last Pickit
detection. Each object cloud is shown in a different color. 

For all engines, it overlays the Pick frame of each object with
the picking order identifiers.

For the Pickit Flex and Pattern engines, it overlays a 2D or 3D model
of the geometric shape (e.g. cylinder, rectangle). For the Teach engine,
it overlays the 3D model cloud. They are colored according to the
following criteria:

-  Green: Valid object
-  Red: Invalid object
-  Orange: Unpickable object, e.g. due to collisions between robot tool
   and bin or other objects. When this is the case, the ROI box and
   robot tool are also rendered in orange. 

The objects view also renders the same additional elements listed for
the the 3D view.

|image6|

Model view
~~~~~~~~~~

Visualizes the taught model together with its Reference frame and Pick
frame. The model bounding box is shown in dashed green lines to indicate
the extent of the model and help detect undesired outliers in models.

This view is only available for the Pickit Teach detection engine.

|image7|

Mentioned articles

What to read next

| `Pickit detection
  grid <https://support.pickit3d.com/article/167-the-pick-it-detection-grid>`__
| `Save
  snapshot <https://support.pickit3d.com/article/168-saving-a-snapshot-in-pick-it>`__\ ` <https://support.pickit3d.com/article/41-attaching-the-roi-box-to-the-robot-base-for-binpicking-objects-from-a-big-bin>`__

| `Configuration <https://support.pickit3d.com/article/157-configuration>`__
| `Region of
  Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
| `Detection: Pickit
  Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
| `Detection:
  Pickit Pattern <https://support.pickit3d.com/article/161-detection-pick-it-pattern>`__
| `Detection:
  Pickit Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb7c1e042863075092367b/file-uCyUdZ21AI.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb78a32c7d3a0e936720ce/file-kQxzHYCzww.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb7d9c2c7d3a0e936720f7/file-o9ZtulH6qG.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb7eed2c7d3a0e93672106/file-dPrGjlK8bo.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb826b2c7d3a0e93672139/file-3RDqv4S7jW.png
.. |image5| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb83862c7d3a0e9367214d/file-CR9uxSjQqb.png
.. |image6| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb844f2c7d3a0e9367215a/file-2C0Pd9CmYB.png
.. |image7| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5acb87c50428630750923742/file-IF4uReyneJ.png

