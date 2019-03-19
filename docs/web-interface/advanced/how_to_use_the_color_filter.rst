How to use the color filter
===========================

The color filter can be used to explicitly include or exclude points
from a certain color. Several use cases for the color filter are:

-  Excluding parts of the bin
-  Detection of thin parts on a flat surface

.. raw:: html

   <div class="callout-yellow">

**Note:** The color filter is a **light dependent solution**. This
requires very stable light conditions for continuous results. 

.. raw:: html

   </div>

Example of detecting thin parts on a flat surface
-------------------------------------------------

|image0|

This is an example case where we want to detect thin parts at the bottom
of a bin. There are several problems that need to be solved:

-  The bottom of the bin is not straight, this results in parts of the
   bottom being visible in the points view.
-  Because of the thin parts it's hard to distinguish them from the
   bottom

1. Define your ROI
~~~~~~~~~~~~~~~~~~

|image1|

When   `defining the
ROI <http://support.pickit3d.com/article/42-define-the-boundaries-of-your-application-with-the-roi-box?auth=true>`__
in a normal way we can see 2 problems:

-  We still see some parts of the bottom in the Points view
-  The point cloud of our parts is not very good.

In a normal situation we can increase the Z-min of the ROI to remove the
bottom, or lower the Z-min to make the parts more visible.

2. Lower the Z-min of the ROI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

|image2|

We lower the Z-min of the ROI to include the whole bottom of the bin,
this makes our point cloud unusable for detections.

3. Exclude the color
~~~~~~~~~~~~~~~~~~~~

|image3|

We can exclude all the points of the yellow bin by activating the color
filter: on the Region of Interest page we select the Color filter tab
and check the Color Filter checkbox.

#. Open the 2D view and click with your mouse cursor on the color you
   would like to exclude
#. Set the switch to Exclude as we want to remove all points of that
   specific color
#. Adjust the Threshold slider to adjust the range of color that will be
   excluded
#. Go back to the Points view and press the Check button to check the
   results.
#. Adjust the Threshold until only the parts are visible.

The result is that our parts are very visible with a very nice point
cloud without parts of the bin being visible.

|image4|

Mentioned articles

What to read next

| 

| `Region of
  Interest <https://support.pickit3d.com/article/159-region-of-interest>`__
| `Detection: Pick-it
  Flex <https://support.pickit3d.com/article/160-detection-pick-it-flex>`__
| `Detection:
  Pick-it Pattern <https://support.pickit3d.com/article/161-detection-pick-it-pattern>`__
| `Detection:
  Pick-it Teach <https://support.pickit3d.com/article/162-detection-pick-it-teach>`__

.. |image0| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5975f0e02c7d3a73488b5397/file-cKtGY3f5zJ.png
.. |image1| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5975eeaa042863033a1b53d1/file-A6K5LHfoqe.png
.. |image2| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5975eee7042863033a1b53d3/file-0a8p9x9nQ0.png
.. |image3| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5975f44b2c7d3a73488b53a8/file-uScqv5wkdb.png
.. |image4| image:: https://s3.amazonaws.com/helpscout.net/docs/assets/583bf3f79033600698173725/images/5975ef102c7d3a73488b5393/file-5F97OSkBI7.png

