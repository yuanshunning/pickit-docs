.. _advanced-roi-filters:

Advanced ROI filters
--------------------

There are a number of advanced Region of Interest filters used for
excluding points \ **inside the ROI box**.

-  :ref:`Flat-curved-region-filter`
-  :ref:`Dynamic-box-based-roi-filter`
-  :ref:`Point-based-roi-filter`
-  :ref:`Plane-based-roi-filter`
-  :ref:`Sphere-based-roi-filter`

.. _Flat-curved-region-filter:

Flat/curved region filter
~~~~~~~~~~~~~~~~~~~~~~~~~

Removes points that belong to flat regions / curved regions, the
curvature can be adjusted with the slider. Higher the Curvature
threshold the bigger the rejected point area.

.. note:: This filter is applied to every detection.

.. _Dynamic-box-based-roi-filter:

Dynamic Box-based ROI filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Removes all points in the point cloud that are located below the topmost
point minus the threshold distance. Located below, refers here to points
that have a smaller value for their z-coordinate when taking the Pickit
reference frame as a reference.

This feature is handy during depalletizing to force it picking layer by
layer.

.. note:: This filter is applied to every detection.

.. _Point-based-roi-filter:

Point-based ROI filter
~~~~~~~~~~~~~~~~~~~~~~

Removes all points located close to a point present in an image of the
empty workspace.

.. note:: This filter is only applied once when you press :guilabel:`Teach Workspace`.

.. _Plane-based-roi-filter:

Plane-based ROI filter
~~~~~~~~~~~~~~~~~~~~~~

Removes all points in the point cloud that are located below the most
dominant plane.

The initialization of the plane-based filtering consists of capturing a
reference image of the empty workspace and finding the dominant plane
through all points within the above-defined region of interest box.

.. note:: This filter is only applied once when you press :guilabel:`Teach Workspace`.

.. _Sphere-based-roi-filter:

Sphere-based ROI filter
~~~~~~~~~~~~~~~~~~~~~~~

Removes all points in the point cloud that are located outside the
dominant spherical shape found in the region of interest box.

The initialization of the sphere-based filtering consists of capturing a
reference image of the empty workspace and finding the dominant sphere
through all points within the above-defined region of interest box.

.. note:: This filter is only applied once when you press :guilabel:`Teach Workspace`.