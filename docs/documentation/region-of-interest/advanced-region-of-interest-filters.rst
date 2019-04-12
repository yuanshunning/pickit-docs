Advanced ROI filters
====================

There are a number of advanced Region of Interest filters used for
excluding points \ **inside the ROI box**.

-  `Flat/curved region filter <#flat-curved>`__
-  `Dynamic Box-based ROI filter <#dynamic>`__
-  `Point-based ROI filter <#point-based>`__
-  `Plane-based ROI filter <#plane-based>`__
-  `Sphere-based ROI filter <#sphere-based>`__

Flat/curved region filter
-------------------------

Removes points that belong to flat regions / curved regions, the
curvature can be adjusted with the slider. Higher the Curvature
threshold the bigger the rejected point area.

.. raw:: html

   <div class="callout-yellow">

**Note** This filter is applied to every detection.

.. raw:: html

   </div>

Dynamic Box-based ROI filter
----------------------------

Removes all points in the point cloud that are located below the topmost
point minus the threshold distance. Located below, refers here to points
that have a smaller value for their z-coordinate when taking the Pickit
reference frame as a reference.

This feature is handy during depalletizing to force it picking layer by
layer.

.. raw:: html

   <div class="callout-yellow">

**Note** This filter is applied to every detection.

.. raw:: html

   </div>

Point-based ROI filter
----------------------

Removes all points located close to a point present in an image of the
empty workspace.

.. raw:: html

   <div class="callout-yellow">

**Note** This filter is only applied once when you press the **Teach
workspace** button.

.. raw:: html

   </div>

Plane-based ROI filter
----------------------

Removes all points in the point cloud that are located below the most
dominant plane.

The initialization of the plane-based filtering consists of capturing a
reference image of the empty workspace and finding the dominant plane
through all points within the above-defined region of interest box.

.. raw:: html

   <div class="callout-yellow">

**Note** This filter is only applied once when you press the **Teach
workspace** button.

.. raw:: html

   </div>

Sphere-based ROI filter
-----------------------

Removes all points in the point cloud that are located outside the
dominant spherical shape found in the region of interest box.

The initialization of the sphere-based filtering consists of capturing a
reference image of the empty workspace and finding the dominant sphere
through all points within the above-defined region of interest box.

**Note** This filter is only applied once when you press the **Teach
workspace** button.


| `Configuration <https://support.pickit3d.com/article/157-configuration>`__
| `Region of
  Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
| `How to use the color
  filter <https://support.pickit3d.com/article/171-how-to-use-the-color-filter>`__
| `Detection: Pickit
  Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
| `Detection:
  Pickit Pattern <https://support.pickit3d.com/article/161-detection-pick-it-pattern>`__
| `Detection:
  Pickit Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__
