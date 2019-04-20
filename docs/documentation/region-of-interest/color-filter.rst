.. _color-filter:

Color filter
------------

The color filter can be used to explicitly include or exclude points
from a certain color. Several use cases for the color filter are:

-  Excluding parts of the bin
-  Detection of thin parts on a flat surface

.. note:: The color filter is a **light dependent solution**. This
   requires very stable light conditions for continuous results. 

Example of detecting thin parts on a flat surface
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: /assets/images/Documentation/Color-filter-2d.png

This is an example case where we want to detect thin parts at the bottom
of a bin. There are several problems that need to be solved:

-  The bottom of the bin is not straight, this results in parts of the
   bottom being visible in the points view.
-  Because of the thin parts it's hard to distinguish them from the
   bottom

1. Define your ROI
^^^^^^^^^^^^^^^^^^

.. image:: /assets/images/Documentation/Color-filter-points.png

When :ref:`Defining-the-region-of-interest`
in a normal way we can see 2 problems:

-  We still see some parts of the bottom in the Points view
-  The point cloud of our parts is not very good.

In a normal situation we can increase the Z-min of the ROI to remove the
bottom, or lower the Z-min to make the parts more visible.

2. Lower the Z-min of the ROI
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. image:: /assets/images/Documentation/Color-filter-points-lower.png

We lower the Z-min of the ROI to include the whole bottom of the bin,
this makes our point cloud unusable for detections.

3. Exclude the color
^^^^^^^^^^^^^^^^^^^^

.. image:: /assets/images/Documentation/Color-filter-exclude.png

We can exclude all the points of the yellow bin by activating the color
filter: on the Region of Interest page we select the Color filter tab
and check the Color Filter checkbox.

#. Open the 2D view and click with your mouse cursor on the color you
   would like to exclude
#. Set the switch to Exclude as we want to remove all points of that
   specific color
#. Adjust the Threshold slider to adjust the range of color that will be
   excluded
#. Go back to the Points view and press :guilabel:`Detect` to check the
   results.
#. Adjust the Threshold until only the parts are visible.

The result is that our parts are very visible with a very nice point
cloud without parts of the bin being visible.

.. image:: /assets/images/Documentation/Color-filter-points-result.png